# import numpy as np

from operator import or_

class segtree:

    def __init__(self, n,operator,identity):
        nb = bin(n)[2:]
        bc = sum([int(digit) for digit in nb])
        if bc == 1:
            self.num_leaves = 2**(len(nb)-1)
        else:
            self.num_leaves = 2**(len(nb))

        self.array = [identity for i in range(self.num_leaves * 2)]
        self.identity = identity
        self.operator =operator
        self.n = n

    def build(self,init_arr):
        for i in range(self.n):
            self.array[i+self.num_leaves] = init_arr[i]
        for i in range(self.num_leaves):
            pt = self.num_leaves-1-i
            self.array[pt] = self.operator(self.array[pt*2],self.array[pt*2+1])


    def update(self,x,val):
        actual_x = x+self.num_leaves
        # self.array[actual_x] = self.operator(self.array[actual_x],val)
        self.array[actual_x] = val
        while actual_x > 0 :
            actual_x = actual_x//2
            self.array[actual_x] = self.operator(self.array[actual_x*2],self.array[actual_x*2+1])

    def get(self,q_left,q_right,arr_ind=1,leaf_left=0,depth=0):
        width_of_floor = self.num_leaves//(2**depth)
        leaf_right = leaf_left+width_of_floor-1

        if leaf_left > q_right or leaf_right < q_left:
            return  self.identity

        elif leaf_left >= q_left and leaf_right <= q_right:
            return self.array[arr_ind]

        else:
            val_l = self.get(q_left,q_right,2*arr_ind,leaf_left,depth+1)
            val_r = self.get(q_left,q_right,2*arr_ind+1,leaf_left+width_of_floor//2,depth+1)
            return self.operator(val_l,val_r)

    def find(self, l, r):
        #findの方が高速
        l += self.num_leaves
        r += self.num_leaves+1
        ret = self.identity
        while l < r:
            if l & 1:
                ret = self.operator(ret, self.array[l])
                l += 1
            if r & 1:
                r -= 1
                ret = self.operator(ret, self.array[r])
            l //= 2
            r //= 2
        return ret







n = int(input())
s = input()
q = int(input())

tree = segtree(n, or_, 0)
buf = [0 for i in range(n)]

for i in range(n):
    c = ord(s[i]) - 97
    buf[i] = 1<<c


for i in range(26):
    tree.build(buf)




s = list(s)

for i in range(q):
    ty, i, c = input().split()

    if ty == "1":
        i = int(i)
        t = ord(c) - 97
        tree.update(i-1,1<<t)


    else:
        i = int(i)
        c = int(c)
        i -= 1
        c -= 1
        tp = 0
        hoge = tree.get(i,c)
        print(sum(map(int,bin(hoge)[2:])))
