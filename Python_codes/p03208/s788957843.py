
N, K = map(int, input().split())
X = [int(input()) for _ in range(N)]

X.sort()
res = 10 ** 9 + 7
for i in range(N - K + 1):
    res = min(res, X[i + K - 1] - X[i])
print(res)
