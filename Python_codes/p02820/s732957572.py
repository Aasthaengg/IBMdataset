N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
'''
rsp -> 012
'''
dp = [[0] * 3 for i in range(N)]
for i in range(0, K):
    for j in range(i, N, K):
        if j == i:
            if T[j] == 'r':
                dp[j][0] += 0
                dp[j][1] += 0
                dp[j][2] += P
            if T[j] == 's':
                dp[j][0] += R
                dp[j][1] += 0
                dp[j][2] += 0
            if T[j] == 'p':
                dp[j][0] += 0
                dp[j][1] += S
                dp[j][2] += 0
        else:
            dp[j][0] = max(dp[j - K][1], dp[j - K][2])
            dp[j][1] = max(dp[j - K][0], dp[j - K][2])
            dp[j][2] = max(dp[j - K][0], dp[j - K][1])
            if T[j] == 'r':
                dp[j][0] += 0
                dp[j][1] += 0
                dp[j][2] += P
            if T[j] == 's':
                dp[j][0] += R
                dp[j][1] += 0
                dp[j][2] += 0
            if T[j] == 'p':
                dp[j][0] += 0
                dp[j][1] += S
                dp[j][2] += 0

#print(dp)
ans = 0
for i in range(N-K,N):
    ans += max(dp[i])
print(ans)
