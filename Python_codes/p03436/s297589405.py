from collections import deque


def main():
    h, w = map(int, input().split())
    maze = [list(input()) for _ in range(h)]

    white_count = 0
    for r in range(h):
        for c in range(w):
            if maze[r][c] == ".":
                white_count += 1

    q = deque()
    q.append((0, 0))
    dist = [[-1 for _ in range(w)] for _ in range(h)]
    dist[0][0] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nr = r + dr
            nc = c + dc

            if not (0 <= nr < h and 0 <= nc < w):
                continue

            if maze[nr][nc] == "#":
                continue

            if dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))

    if dist[h - 1][w - 1] == -1:
        print(-1)
    else:
        print(white_count - dist[h - 1][w - 1] - 1)


if __name__ == "__main__":
    main()
