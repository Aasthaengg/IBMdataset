from collections import deque

H, W = map(int, input().split())

G = []
G.append(["#" for _ in range(W + 2)])
for i in range(H):
    G.append(["#"] + list(input()) + ["#"])
G.append(["#" for _ in range(W + 2)])

# print(G)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

INF = 10 ** 18
d = [[INF for i in range(W + 2)] for j in range(H + 2)]


def bfs(i, j):
    q = deque()
    q.append((i, j))
    d[i][j] = 0
    while q:
        a, b = q.popleft()
        for k in range(4):
            if G[a + dx[k]][b + dy[k]] == "#":
                continue
            if d[a + dx[k]][b + dy[k]] != INF:
                continue
            d[a + dx[k]][b + dy[k]] = d[a][b] + 1
            q.append((a + dx[k], b + dy[k]))


bfs(1, 1)
# print(d)
# print(d[H][W])

# (H+2)*(W+2) から「経路+1」と、全ての'#'の数を引いたものが答え
if d[H][W] == INF: # 到達できないときは -1を出力
    print(-1)
else:
    ans = (H + 2) * (W + 2)
    ans -= d[H][W] + 1
    cnt = 0
    for h in range(H + 2):
        for w in range(W + 2):
            if G[h][w] == "#":
                cnt += 1
    ans -= cnt
    print(ans)
