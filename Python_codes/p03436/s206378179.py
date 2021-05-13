from queue import Queue
from itertools import product


def main():
    h, w = map(int, input().split())
    grid = ["." * w for _ in range(h)]
    for i in range(h):
        grid[i] = input()
    num_white = 0
    for i, j in product(range(h), range(w)):
        if grid[i][j] == ".":
            num_white += 1
    dist = [[-1] * w for _ in range(h)]
    q = Queue()
    q.put((0, 0))
    dist[0][0] = 1
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]
    while not q.empty():
        i, j = q.get()
        d = dist[i][j]
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < 0 or ni >= h or nj < 0 or nj >= w:
                continue
            if grid[ni][nj] == "#":
                continue
            if dist[ni][nj] != -1 and dist[ni][nj] <= d + 1:
                continue
            dist[ni][nj] = d + 1
            q.put((ni, nj))
    print(num_white - dist[h - 1][w - 1] if dist[h - 1][w - 1] != -1 else -1)


if __name__ == "__main__":
    main()
