import sys

N = int(input())
K = int(input())
X = list(map(int, sys.stdin.readline().rsplit()))

res = 0
for i in range(1, N + 1):
    x = X[i - 1]
    res += min(x * 2, abs(x - K) * 2)

print(res)
