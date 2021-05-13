n,k = map(int,input().split())
a = list(map(int,input().split()))
mod = 10**9+7

class BIT:
    def __init__(self, n):
        self.size = n
        self.tree = [0]*(n+1)
 
    def sum(self, i):
        # [0, i) の要素の総和を返す
        s = 0
        while i>0:
            s += self.tree[i]
            i -= i & -i
        return s
    # 0 index を 1 index に変更  転倒数を求めるなら1を足していく
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i

bit = BIT(2001)
count = [0]*(2001)
t = []
for i in range(n):
    x = a[i]
    count[x] += 1
    t.append(i-bit.sum(x))
    bit.add(x,1)

for i in range(1,2001):
    count[i] += count[i-1]

ans = 0
for i in range(n):
    x = k*(2*t[i]+(k-1)%mod*count[a[i]-1])//2
    ans = (ans+x)%mod
print(ans)
