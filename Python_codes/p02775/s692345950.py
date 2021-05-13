S = input()
S = S[::-1]
S += '0'

n = len(S)
dp = [[10**20 for j in range(2)] for i in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(2):
        x = ord(S[i])-ord('0')
        x += j
        for a in range(10):
            ni = i+1
            nj = 0
            b = a-x
            if b < 0:
                nj = 1
                b += 10
            dp[ni][nj] = min(dp[ni][nj], dp[i][j]+a+b)

print(dp[n][0])
