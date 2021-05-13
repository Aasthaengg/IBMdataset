import numpy as np

n = int(input())
a = np.zeros((n, 3))
for i in range(n):
    a[i][0], a[i][1], a[i][2] = map(int, input().split())
ans = 0
memo = np.zeros((n + 1, 3))
for i in range(1, n + 1):
    for j in range(3):
        for k in range(3):
            if (j == k):
                continue
            memo[i][j] = max(memo[i][j], memo[i - 1][k] + a[i-1][j])

print(int(max(memo[n])))