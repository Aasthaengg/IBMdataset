import itertools

n, m, R = map(int, input().split())
r = list(map(int, input().split()))

dis = [[float("inf") for i in range(n)] for j in range(n)]
for i in range(n):
    dis[i][i] = 0
for i in range(m):
    a, b, c = map(int, input().split())
    dis[a-1][b-1] = c
    dis[b-1][a-1] = c

def warshall_floyd(dis):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    return dis

data = warshall_floyd(dis)
ans = float("inf")
for i in itertools.permutations(r, R):
    num = 0
    for j in range(R - 1):
        num += data[i[j] - 1][i[j + 1] - 1]
    ans = min(ans, num)
print(ans)