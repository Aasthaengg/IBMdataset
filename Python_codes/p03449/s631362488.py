from collections import deque
INF = 10 ** 5
def bfs():
    que = deque([(1, 1)])
    cnt = [[0] * (N + 2) for _ in range(4)]
    cnt[1][1] = A[1][1]
    steps = [(1, 0), (0, 1)]
    while que:
        i, j = que.popleft()
        for di, dj in steps:
            ni, nj = i + di, j + dj
            if cnt[ni][nj] < cnt[i][j] + A[ni][nj]:
                cnt[ni][nj] = cnt[i][j] + A[ni][nj]
                que.append((ni, nj))
    return cnt[2][N]

N = int(input())
A = [[-INF] * (N + 2)]
for _ in range(2):
    a = list(map(int, input().split()))
    A.append([-INF] + a + [-INF])
A.append([-INF] * (N + 2))
res = bfs()
print(res)
