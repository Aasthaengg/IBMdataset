
import collections


def solve(n, k, x, y):
    return min(n, k) * x + max(0, n-k) * y


n = int(input().strip())
k = int(input().strip())
x = int(input().strip())
y = int(input().strip())

print(solve(n, k, x, y))
