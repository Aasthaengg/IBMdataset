from collections import deque

N, X, Y = map(int, input().split())

dist = [[0 for _ in range(N)] for _ in range(N)]
ans = [0 for _ in range(N)]

for i in range(N):
    for j in range(N):
        tmp1 = abs(i - X + 1) + abs(j - Y + 1) + 1
        tmp2 = abs(i - Y + 1) + abs(j - X + 1) + 1

        dist[i][j] = min(abs(i - j), tmp1, tmp2)
        dist[j][i] = min(abs(i - j), tmp1, tmp2)

for i in range(N):
    for j in range(i+1, N):
        ans[dist[i][j]-1] += 1

for i in range(N - 1):
    print(ans[i])