from collections import deque


def main():
    h, w = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    ans = 0

    dist = [[-1 for _ in range(w)] for _ in range(h)]

    black = deque()
    for r in range(h):
        for c in range(w):
            if graph[r][c] == "#":
                black.append((r, c))
                dist[r][c] = 0

    while black:
        r, c = black.popleft()
        ans = max(ans, dist[r][c])
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = r + dr
            nc = c + dc
            if not (0 <= nr < h and 0 <= nc < w):
                continue
            if dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                black.append((nr, nc))

    print(ans)


if __name__ == "__main__":
    main()
