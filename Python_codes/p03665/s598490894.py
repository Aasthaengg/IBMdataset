n, p = map(int, input().split())
A = list(map(int, input().split()))
U = n*100
dp = [0]*(U+1)
dp[0] = 1
for a in A:
    for j in reversed(range(U+1)):
        if 0 <= j-a:
            dp[j] += dp[j-a]
print(sum(dp[p::2]))
