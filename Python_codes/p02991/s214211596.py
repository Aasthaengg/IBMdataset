import sys

input = sys.stdin.readline

N, M = map(int, input().split())
L = [[] for i in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    L[a].append(b)

# print(L)
S, T = map(int, input().split())
dist = [[10**9 for i in range(N + 1)] for j in range(3)]
dist[0][S] = 0
# print(dist)
Q = []
for i in L[S]:
    Q.append([i, S, 0])

for i in range(10 ** 7):
    if len(Q) == i:
        break
    if dist[(Q[i][2] + 1) % 3][Q[i][0]] == 10**9:
        dist[(Q[i][2] + 1) % 3][Q[i][0]] = dist[(Q[i][2]) % 3][Q[i][1]] + 1
        for j in L[Q[i][0]]:
            if dist[(Q[i][2] + 2) % 3][j] == 10**9:
                Q.append([j, Q[i][0], Q[i][2] + 1])
if dist[0][T] % 3 == 0:
    print(dist[0][T] // 3)
else:
    print(-1)
    #print(dist[0][:30])