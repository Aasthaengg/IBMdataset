
from collections import deque
def resolve():
    INF = 1 << 60
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]

    dist = [[INF] * W for _ in range(H)]
    dist[0][0] = 0 if G[0][0] == "." else 1

    q = deque()
    q.append((dist[0][0], 0, 0))
    drc = [(1, 0), (0, 1)]
    while q:
        cost, y, x = q.popleft()
        for dy, dx in drc:
            ny = y + dy
            nx = x + dx
            if y + dy >= H or x + dx >= W:
                continue
            nx_cost = cost if G[y][x] == G[ny][nx] else cost + 1
            if nx_cost < dist[ny][nx]:
                dist[ny][nx] = nx_cost
                q.append((dist[ny][nx], ny, nx))

    ans = (dist[H - 1][W - 1] + 1) // 2
    print(ans)


if __name__ == "__main__":
    resolve()
