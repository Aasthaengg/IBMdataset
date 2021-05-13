n, m = map(int, input().split())
dp = [float("inf") for i in range(2 ** n)]
dp[0] = 0

for i in range(m):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    num = 0
    for j in range(b):
        num += 2 ** (c[j] - 1)
    for k in range(2 ** n):
        dp[k | num] = min(dp[k | num], dp[k] + a)
if dp[2 ** n - 1] == float("inf"):
    print(-1)
else:
    print(dp[2 ** n - 1])