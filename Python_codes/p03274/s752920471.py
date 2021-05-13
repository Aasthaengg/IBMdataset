import sys

N, K = map(int, input().split())
X = list(map(int, sys.stdin.readline().rsplit()))

res = 10 ** 10
for i in range(N):
    if i + K - 1 < N:
        a, b = X[i], X[i + K - 1]
        if b <= 0:
            res = min(res, abs(a))
        elif 0 <= a:
            res = min(res, b)
        else:
            res = min(res, 2 * abs(a) + abs(b), abs(a) + abs(b) * 2)

print(res)
