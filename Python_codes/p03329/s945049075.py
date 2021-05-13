import sys
def I(): return int(sys.stdin.readline().rstrip())

N = I()

A = [1,6,9,36,81,216,729,1296,6561,7776,46656,59049]  # 引き出せる金額

dp = [0]*(N+1)  # dp[i] = i円引き出すのに必要な操作の回数
for i in range(N+1):
    if i == 0:
        continue
    else:
        a = N
        for j in A:
            if i >= j:
                a = min(a,dp[i-j]+1)
        dp[i] = a

print(dp[N])
