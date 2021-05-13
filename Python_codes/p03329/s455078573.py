N = int(input())
ans = float('inf')
ls = []
l = [1]
tmp = 6
while tmp <= 100000:
    l += [tmp]
    tmp *= 6
tmp = 9
while tmp <= 100000:
    l += [tmp]
    tmp *= 9

dp = [float('inf')]*(N+1)
dp[0] = 0
dp[1] = 1
for i in range(N+1):
    for n in l:
        if i-n >= 0:
            dp[i] = min(dp[i],dp[i-n]+1)
print(dp[N])