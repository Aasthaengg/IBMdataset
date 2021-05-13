ii = lambda : int(input())
li = lambda : list(map(int,input().split()))

from collections import deque

class tree:
    def __init__(self,n):
        self.n = n
        self.arr = [[] for i in range(self.n)]
        self.root = [-1]*n

    def add_arr(self, u, v):
        if v[0] != 0:
            self.arr[u-1] = v[1:]

n = ii()
t = tree(n)
for i in range(n):
    uk = li()
    t.add_arr(uk[0],uk[1:])
l = deque()
l.append(0)
t.root[0] = 0
while len(l)>0:
    p = l.popleft()
    for i in t.arr[p]:
        if t.root[i-1] == -1:
            t.root[i-1] = t.root[p]+1
            l.append(i-1)

for k,i in enumerate(t.root):
    print(k+1,i)
