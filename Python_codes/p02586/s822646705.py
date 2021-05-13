import sys
import time
s1 = time.time()
*data, = map(int, sys.stdin.read().split()[::-1])

def inp():
    global data
    return data.pop()
R, C, k = inp(), inp(), inp()
grid = [[0] * C for _ in range(R)]

for _ in range(k):
    ri, ci, v = inp(), inp(), inp()
    grid[ri - 1][ci - 1] = v


dp = []
for _ in range(4):
    dp.append([[0] * (C + 1) for _ in range(R + 1)])

# print(time.time() - s1)
mx = 0
for row in range(1, R + 1):
    for col in range(1, C + 1):
        level = 0
        dp[1][row][col] = max(dp[1][row][col], dp[3][row - 1][col] + grid[row - 1][col - 1])
        dp[0][row][col] = max(dp[0][row][col], dp[3][row - 1][col])
        level = 1
        v = grid[row - 1][col - 1]
        while level < 4:
            dp[level][row][col] = max(
                dp[level - 1][row][col],
                dp[level][row][col],
                dp[level][row][col - 1],
                dp[level - 1][row][col - 1] + v,
            )
            mx = max(mx, dp[level][row][col])
            level += 1

# print(time.time() - s1)
print(mx)
