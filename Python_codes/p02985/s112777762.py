class Cmb:
    def __init__(self, N, mod=10**9+7):
        self.fact = [1,1]
        self.fact_inv = [1,1]
        self.inv = [0,1]
        
        """ 階乗を保存する配列を作成 """
        for i in range(2, N+1):
            self.fact.append((self.fact[-1]*i) % mod)
            self.inv.append((-self.inv[mod%i] * (mod//i))%mod)
            self.fact_inv.append((self.fact_inv[-1]*self.inv[i])%mod)
    
    """ 関数として使えるように、callで定義 """
    def __call__(self, n, r, mod=10**9+7):
        if (r<0) or (n<r):
            return 0
        return self.fact[n] * self.fact_inv[n-r] % mod

from collections import deque
n,k = map(int,input().split())
mod = 10**9 + 7
es = [[] for _ in range(n+1)]
d = [0]*(n+1)
for _ in range(n-1):
    a,b = map(int,input().split())
    es[a].append(b)
    es[b].append(a)
    d[a] += 1
    d[b] += 1

root = -1
for i in range(1, n+1):
    if d[i] == 1:
        root = i
        break

num_child = [0]*(n+1)
que = deque([])
for c in es[root]:
    que.append((root, c))

while que:
    p,c = que.pop()
    num_child[p] += 1
    for nx in es[c]:
        if nx!=p:
            que.append((c, nx))

c = Cmb(N=k)
ans = k

for e,child in enumerate(num_child[1:]):
    if e+1==root:
        cand = k-1
    else:
        cand = k-2
    if child==0:
        continue
    else:
        ans = ans*(c(cand, child)) % mod

print(ans%mod)