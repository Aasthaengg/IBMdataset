from bisect import bisect_left
N, M = map(int, input().split())
G = [[] for _ in range(N)]
P = [0]*M
Y = [0]*M
for i in range(M):
    P[i], Y[i] = map(int, input().split())
    G[P[i]-1].append(Y[i])

for i in range(N):
    G[i].sort()

for i in range(M):
    right = bisect_left(G[P[i]-1], Y[i])+1
    print(str(P[i]).rjust(6, '0')+str(right).rjust(6, '0'))
