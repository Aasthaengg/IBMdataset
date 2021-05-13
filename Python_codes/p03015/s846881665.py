S = input()
C = 10**9+7
T = S[::-1]
N = len(S)
dp = [0]*N
dp[0] = 1+2*(int(T[0]))

for i in range(1, N):
    if T[i] == '0':
        dp[i] = dp[i-1]
    else:
        dp[i] = (pow(3, i, C)+2*dp[i-1]) % C
print(dp[-1])