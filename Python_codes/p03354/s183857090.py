import sys
sys.setrecursionlimit(1000000)
def par(a):
    if P[a] < 0: return a
    t = par(P[a])
    P[a] = t
    return t
def unite(a, b):
    if par(a) == par(b): return 0
    if P[par(b)] == P[par(a)]:
        P[par(b)] = par(a)
        P[par(a)] -= 1
    elif P[par(b)] > P[par(a)]:
        P[par(b)] = par(a)
    else:
        P[par(a)] = par(b)

N, M = map(int, input().split())
P = [-1 for i in range(N)]
A = [int(a)-1 for a in input().split()]
for _ in range(M):
    x, y = map(int, input().split())
    unite(x-1, y-1)

X = [[] for _ in range(N)]
Y = [[] for _ in range(N)]
for i in range(N):
    X[par(i)].append(i)
    Y[par(i)].append(A[i])

ans = 0
for i in range(N):
    ans += len(set(X[i]) & set(Y[i]))

print(ans)

