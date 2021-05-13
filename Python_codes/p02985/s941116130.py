import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

MOD = 10**9 + 7

N,K = map(int,readline().split())
AB = map(int,read().split())

if N == 1:
    print(K)
    exit()
if K == 1:
    print(0)
    exit()

def cumprod(arr,MOD):
    L = len(arr); Lsq = int(L**.5+1)
    arr = np.resize(arr,Lsq**2).reshape(Lsq,Lsq)
    for n in range(1,Lsq):
        arr[:,n] *= arr[:,n-1]; arr[:,n] %= MOD
    for n in range(1,Lsq):
        arr[n] *= arr[n-1,-1]; arr[n] %= MOD
    return arr.ravel()[:L]

def make_fact(U,MOD):
    x = np.arange(U,dtype=np.int64); x[0] = 1
    fact = cumprod(x,MOD)
    x = np.arange(U,0,-1,dtype=np.int64); x[0] = pow(int(fact[-1]),MOD-2,MOD)
    fact_inv = cumprod(x,MOD)[::-1]
    return fact,fact_inv

fact,fact_inv = make_fact(K+10,MOD)

graph = [[] for _ in range(N+1)]
for a,b in zip(AB,AB):
    graph[a].append(b)
    graph[b].append(a)

# 次数1の頂点を根とする
deg = [len(x) for x in graph]
for i,x in enumerate(deg):
    if x == 1:
        break
root = i

parent = [0] * (N+1)
ts = [root]
stack = [root]
while stack:
    x = stack.pop()
    for y in graph[x]:
        if y == parent[x]:
            continue
        parent[y] = x
        stack.append(y)
        ts.append(y)

perm = np.zeros(N+K+10,np.int64)
perm[:K-1] = fact[K-2] * fact_inv[K-2::-1] % MOD
perm = perm.tolist()

dp = [1] * (N+1)
for v in ts[::-1]:
    if v == root:
        break
    d = deg[v]
    dp[v] *= perm[d-1]; dp[v] %= MOD
    p = parent[v]
    dp[p] *= dp[v]; dp[p] %= MOD

x = dp[root]
x *= K*(K-1)%MOD
x %= MOD
print(x)