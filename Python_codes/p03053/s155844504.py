from collections import deque
def solve():
    max_cost = 0
    stack = deque()
    used = [[False for _ in range(W)] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if A[i][j] == '.':
                continue
            stack.append([(i, j), 0])
            used[i][j] = True
    while stack:
        (i, j), cost = stack.popleft()
        max_cost = max(max_cost, cost)
        for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if not 0 <= x < H or not 0 <= y < W or used[x][y]:
                continue
            stack.append([(x, y), cost + 1])
            used[x][y] = True
    print(max_cost)

if __name__ == "__main__":
    H, W = map(int, input().split())
    A = []
    for _ in range(H):
        A.append(list(input()))
    solve()