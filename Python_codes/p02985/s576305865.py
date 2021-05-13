MOD = 10**9 + 7
import sys
from collections import defaultdict, deque
input = sys.stdin.readline
N,K = map(int,input().split())

num = 100010
fact = [1] * (num+1)
ifact = [1] * (num+1)
inv = [pow(i,MOD-2,MOD) for i in range(num+1)]
for i in range(1,num+1):
    fact[i] = (fact[i-1] * i) % MOD
    ifact[i] = (ifact[i-1] * inv[i]) % MOD

def nPr(n,r):
    return (fact[n] * ifact[n-r]) % MOD

g = defaultdict(list)
for i in range(N-1):
    a,b = map(int,input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1,N+1):
    nnode = len(g[i])+1
    if nnode > K:
        print(0)
        exit()

dq = deque([1])

visited = [False] * (N+1)

ans = nPr(K,len(g[1])+1)
while dq:
    v = dq.popleft()
    visited[v] = True
    if v != 1:
        npattern = len(g[v])-1
        ans *= nPr(K-2,npattern)
        ans %= MOD
    for nv in g[v]:
        if visited[nv]:
            continue
        dq.append(nv)
print(ans)



