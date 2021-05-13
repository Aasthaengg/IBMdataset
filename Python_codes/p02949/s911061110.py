import sys
input = sys.stdin.readline

INF = 10**18

N, M, P = map(int, input().split())
G = []
for i in range(M):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    G.append((a, b, c-P))
D = [0]*N
for i in range(N):
    D[i] = -INF
D[0] = 0
for i in range(N):
    for j in range(M):
        fr, to, cost = G[j]
        if D[fr] != -INF and D[fr]+cost > D[to]:
            D[to] = D[fr]+cost
for _ in range(N):
    for j in range(M):
        fr, to, cost = G[j]
        if D[fr] != -INF and D[fr]+cost > D[to]:
            D[to] = INF
            if to == N-1:
                print(-1)
                exit()
if D[N-1] < 0:
    print(0)
else:
    print(D[N-1])
