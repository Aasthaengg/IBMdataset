from collections import deque

H, W = map(int, input().split())
X = [input() for _ in range(H)]


def solve_maze(s):
    bias = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    inf = 10 ** 9

    d = [[inf] * W for _ in range(H)]
    d[s[0]][s[1]] = 0

    q = deque()
    q.append(s)
    while q:
        u, v = q.popleft()
        for i, j in bias:
            if (0 <= u + i < H and 0 <= v + j < W
                    and X[u + i][v + j] == "."
                    and d[u + i][v + j] > d[u][v] + 1):
                d[u + i][v + j] = d[u][v] + 1
                q.append((u + i, v + j))

    res = 0
    for i in range(H):
        for j in range(W):
            if d[i][j] < inf:
                res = max(res, d[i][j])
                
    return res


ans = 0
for i in range(H):
    for j in range(W):
        if X[i][j] == ".":
            ans = max(ans, solve_maze((i, j)))

print(ans)
