N = int(input())

a,b,c = list(map(int, input().split()))
ai, bi, ci = 0,1,2

dp = [[0]*3 for _ in range(N)]
dp[0][ai] = a
dp[0][bi] = b
dp[0][ci] = c

for day in range(1, N):
    a,b,c = list(map(int, input().split()))
    dp[day][ai] += max(dp[day-1][bi], dp[day-1][ci]) + a
    dp[day][bi] += max(dp[day-1][ci], dp[day-1][ai]) + b
    dp[day][ci] += max(dp[day-1][ai], dp[day-1][bi]) + c

print(max(dp[-1]))