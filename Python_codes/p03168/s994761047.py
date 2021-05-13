import sys
# 許容する再帰処理の回数を変更
sys.setrecursionlimit(10**5+10)
# input処理を高速化する
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
p = list(map(float, input().split()))

#dp[i][j]は最初のi枚まで投げてj枚表になる確率
#初期化
dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
#初期条件 0枚投げたとき0枚表→1
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        dp[i+1][j] += dp[i][j] * (1 - p[i])
        dp[i+1][j+1] += dp[i][j] * p[i]

#i == N で j >= (N+1)/2 のものを足し合わせる
ans = 0
for j in range((N+1)//2, N+1):
    ans += dp[N][j]
print(ans)