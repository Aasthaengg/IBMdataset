N, M = map(int, input().split())
As = sorted(list(map(int, input().split())), reverse=True)

INF = 10**9
matches = [2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = [-INF for _ in range(N+100)]
dp[0] = 0

for i in range(N+1):
    for a in As:
        dp[i+matches[a-1]] = max(dp[i+matches[a-1]], dp[i]+1)

ans = ''
while N != 0:
    for a in As:
        if dp[N-matches[a-1]] == dp[N]-1:
            ans = ans+str(a)
            N -= matches[a-1]
            break

print(ans)
