from collections import deque

def solve():
    if s[0][0] == '#':
        print(-1)
        return

    stack = deque()
    stack.append([0, 0, 0])
    used = [[False for _ in range(W)] for _ in range(H)]
    costs = [[float('inf') for _ in range(W)] for _ in range(H)]
    while stack:
        i, j, cost = stack.popleft()
        costs[i][j] = cost
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if not 0 <= x < H or not 0 <= y < W or used[x][y] or s[x][y] == '#':
                continue
            stack.append([x, y, cost + 1])
            used[x][y] = True

    print(dot_num - 1 - costs[H - 1][W - 1] if costs[H - 1][W - 1] != float('inf') else -1)

if __name__ == "__main__":
    H, W = map(int, input().split())
    s = []
    dot_num = 0
    for _ in range(H):
        tmp = list(input())
        dot_num += tmp.count('.')
        s.append(tmp)
    solve()