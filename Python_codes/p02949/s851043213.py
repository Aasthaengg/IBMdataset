import sys

INF = 10 ** 9
N, M, P = map(int,input().split())

edges = []

for _ in range(M):
    A, B, C = map(int,input().split())
    edges.append([A-1, B-1, P-C])

flag1 = [0] * N
flag2 = [0] * N
flag = [0] * N

flag1[0] = 1
flag2[N-1] = 1

for i in range(N-1):
    for j in range(M):
        edge = edges[j]
        if flag1[edge[0]]:
            flag1[edge[1]] = 1
        if flag2[edge[1]]:
            flag2[edge[0]] = 1

for i in range(N):
    if flag1[i] and flag2[i]:
        flag[i] = 1

d = [INF] * N
d[0] = 0
k = None

for i in range(N):
    for j in range(M):
        edge = edges[j]
        if d[edge[1]] > d[edge[0]] + edge[2]:
            d[edge[1]] = d[edge[0]] + edge[2]
            if i == N - 1 and flag[edge[1]]:
                print(-1)
                sys.exit()

print(max(-1 * d[N-1], 0))