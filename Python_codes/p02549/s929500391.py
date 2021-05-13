#bitでタコ殴りにする
class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
        self.depth = n.bit_length()
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
 
    def lower_bound(self, x):
        """ 累積和がx以上になる最小のindexと、その直前までの累積和 """
        sum_ = 0
        pos = 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.tree[k] < x:
                sum_ += self.tree[k]
                pos += 1 << i
        return pos + 1, sum_

m=998244353    
N,K=map(int,input().split())
bit = Bit(N)
bit.add(1,1)#初期値　はじめは１
period = []
for _ in range(K):#動ける区間の記憶
    l,r=map(int,input().split())
    period.append((l,r))
for i in range(2,N+1):#2からNまで見ていく。もらうDP
    for l,r in period:
        rx = max(0,i-l)
        lx = max(0,i-r-1)
        if rx==0:
            tmp_r = 0
        else:
            tmp_r = bit.sum(rx)
        if lx == 0:
            tmp_l = 0
        else:
            tmp_l = bit.sum(lx)
        bit.add(i,(tmp_r-tmp_l)%m)
ans = (bit.sum(N)-bit.sum(N-1))%m
print(ans)



