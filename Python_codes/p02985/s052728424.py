import sys
import numpy as np

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

MOD = 10 ** 9 + 7

def cmb(n, k):
    if k < 0 or k > n: return 0 
    return fact[n] * fact_inv[k] % MOD * fact_inv[n-k] % MOD

def cumprod(arr, MOD):
    L = len(arr); Lsq = int(L**.5+1)
    arr = np.resize(arr, Lsq**2).reshape(Lsq, Lsq)
    for n in range(1, Lsq):
        arr[:, n] *= arr[:, n-1]; arr[:, n] %= MOD
    for n in range(1, Lsq):
        arr[n] *= arr[n-1, -1]; arr[n] %= MOD
    return arr.ravel()[:L]

def make_fact(U, MOD):
    x = np.arange(U, dtype=np.int64); x[0] = 1
    fact = cumprod(x, MOD)
    x = np.arange(U, 0, -1, dtype=np.int64); x[0] = pow(int(fact[-1]), MOD-2, MOD)
    fact_inv = cumprod(x, MOD)[::-1]
    return fact, fact_inv

def permutation(n, x, mod=10**9+7):
    # nPx 順列　ex) permutaion(5, 2) = 20
    tmp = 1
    for i in range(n, n-x, -1):
        tmp = (tmp * i) % mod
    return tmp

U = 10 ** 5 + 10 # 階乗テーブルの上限
fact, fact_inv = make_fact(U, MOD)

N, K = lr()
graph = [[] for _ in range(N+1)] # 1-indexed
for _ in range(N-1):
    a, b = lr()
    graph[a].append(b)
    graph[b].append(a)

answer = K # rootの色の塗り方
if K-1-len(graph[1]) < 0:
    answer = 0
else:
    answer *= fact[K-1] * fact_inv[K-1-len(graph[1])] % MOD
answer %= MOD
root = 1
stack = []
for child in graph[1]:
    if len(graph[child]) > 1:
        stack.append((child, 1))
while stack:
    cur, p = stack.pop()
    l = len(graph[cur])
    if K-2-(len(graph[cur])-1) < 0:
        answer = 0
    elif l > 1:
        answer *= fact[K-2] * fact_inv[K-2-(len(graph[cur])-1)] % MOD
    for child in graph[cur]:
        if child == p:
            continue
        stack.append((child, cur))
    answer %= MOD

print(answer%MOD)
# 10
