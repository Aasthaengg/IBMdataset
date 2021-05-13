import sys

readline = sys.stdin.readline
n, m = map(int, readline().split())
grid = []
for _ in range(n):
    row = readline()
    real_row = [c for c in row if c != "\n"]
    grid.append(real_row)
dp = []
sys.setrecursionlimit(10**7)

for _ in range(n):
    temp = []
    for j in range(m):
        temp.append(-1)
    dp.append(temp)


def traverse(i, j):
    path = 0
    if i < n-1 and j < m-1:
        if dp[i][j] != -1:
            return dp[i][j]
    if i == n - 1 and j == m - 1:
        return 1
    elif i == n - 1:
        if grid[i][j + 1] != "#":
            path += traverse(i, j + 1)
    elif j == m - 1:
        if grid[i + 1][j] != "#":
            path += traverse(i + 1, j)
    else:
        if grid[i + 1][j] != "#":
            path += traverse(i + 1, j)
        if grid[i][j + 1] != "#":
            path += traverse(i, j + 1)
    dp[i][j] = path
    return path % (10 ** 9 + 7)


print(traverse(0, 0))
