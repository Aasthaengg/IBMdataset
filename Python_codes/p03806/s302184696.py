inf = float('inf')

N, Ma, Mb = map(int, input().split())
dp = [[inf] * (400 + 1) for _ in range(400 + 1)]
dp[0][0] = 0

max_a = 0
max_b = 0
for i in range(N):
    a, b, c = map(int, input().split())
    max_a += a
    max_b += b
    for j in reversed(range(max_a + 1 - a)):
        for k in range(max_b + 1 - b):
            if dp[j][k] == inf: continue
            dp[j + a][k + b] = min(dp[j][k] + c, dp[j + a][k + b])

j = Ma
k = Mb
ans = inf
while j < 400 + 1 and k < 400 + 1:
    ans = min(ans, dp[j][k])
    j += Ma
    k += Mb

print(-1 if ans == inf else ans)
# print(dp)
