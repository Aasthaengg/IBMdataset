import sys
from collections import deque

input = sys.stdin.readline


def main():
    H, W = map(int, input().split())
    S = [None] * (H + 2)
    S[0] = S[-1] = "x" * (W + 2)
    for i in range(1, H + 1):
        S[i] = "".join(["x", input().rstrip(), "x"])

    group = []
    visited = [[True] + [False] * W + [True] for _ in range(H + 2)]
    visited[0] = visited[-1] = [True] * (W + 2)
    for h in range(1, H + 1):
        for w in range(1, W + 1):
            if visited[h][w]:
                continue
            queue = deque([(h, w, S[h][w])])
            group.append({"#": 0, ".": 0})
            while queue:
                y, x, s = queue.popleft()
                if visited[y][x]:
                    continue
                visited[y][x] = True
                group[-1][s] += 1
                for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    yy, xx = y + i, x + j
                    if visited[yy][xx]:
                        continue
                    if s == "#" and S[yy][xx] == ".":
                        queue.append((yy, xx, "."))
                    elif s == "." and S[yy][xx] == "#":
                        queue.append((yy, xx, "#"))

    ans = 0
    for g in group:
        ans += g["#"] * g["."]
    print(ans)


if __name__ == "__main__":
    main()
