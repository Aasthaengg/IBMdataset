import sys
sys.setrecursionlimit(10**7)
N,Q = list(map(int,input().split()))
AB = [list(map(int,input().split())) for _ in range(N-1)]
PX = [list(map(int,input().split())) for _ in range(Q)]

X = {i+1:0 for i in range(N)}
for px in PX:
    X[px[0]] += px[1]

G = {i+1:[] for i in range(N)}
for ab in AB:
    G[ab[0]].append(ab[1])
    G[ab[1]].append(ab[0])

seen = [False]*N
W = [0]*N

def dfs(G, W, v, w):
    seen[v-1] = True
    W[v-1] = w+X[v]
    for nv in G[v]:
        if seen[nv-1]:
            continue
        dfs(G, W, nv, W[v-1])

dfs(G, W, 1, 0)

print(*W)