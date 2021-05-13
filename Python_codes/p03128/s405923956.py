N, M = map(int, input().split())
A = list(map(int, input().split()))
dp = [-1] * (N + 1)
dp[0] = 0
match = [2, 5, 5, 4, 5, 6, 3, 7, 6]
mn = []
for a in A:
    mn.append([match[a-1],a])
for i in range(2, N+1):
    for m, n in mn:
        if i-m  >= 0:
            dp[i] = max(dp[i],dp[i-m]*10+n)       
print(dp[-1])