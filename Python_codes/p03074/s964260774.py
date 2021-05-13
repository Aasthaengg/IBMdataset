import numpy as np

n, k = map(int, input().split())
s = [int(x) for x in input()]

memo = np.zeros(10 ** 5 + 1, dtype=np.int64)
W = min(2 * k, 10 ** 5)

current = 1
p = 0

for x in s:
    if x == current:
        memo[p] += 1
    else:
        current = 1 - current
        p += 1
        memo[p] += 1

ans = memo[:W + 1].sum()
x = ans

for r in range(2, 10 ** 5 + 1, 2):
    if r + W > 10 ** 5:
        break
    x = x - memo[r - 2] - memo[r - 1] + memo[r + W] + memo[r + W - 1]
    if x > ans:
        ans = x
print(ans)
