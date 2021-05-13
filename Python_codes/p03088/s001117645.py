import sys
input = lambda: sys.stdin.readline().rstrip()

MOD = 10 ** 9 + 7

N = int(input())

#A=0, G=1, C=2, T=3と考える

dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(N+1)]

#Tは制約に入らないので、スタートをTTT+Sみたいな感じに考える。ここで0とか1とか2を使うといらないところでcontinueしてしまう。
dp[0][3][3][3] = 1

for l in range(N):
    #左から3番目
    for last3 in range(4):
        #左から2番目
        for last2 in range(4):
            #左から1番目
            for last1 in range(4):
                #条件に当てはまるものないときはcontinue
                if dp[l][last3][last2][last1] == 0: 
                    continue
                #追加する文字
                for now in range(4):
                    if last2 == 0 and last1 == 2 and now == 1: continue
                    if last2 == 0 and last1 == 1 and now == 2: continue
                    if last2 == 2 and last1 == 0 and now == 1: continue
                    if last3 == 0 and last1 == 2 and now == 1: continue
                    if last3 == 0 and last2 == 2 and now == 1: continue

                    dp[l+1][last2][last1][now] += dp[l][last3][last2][last1]
                    dp[l+1][last2][last1][now] %= MOD

#長さNの全部の答えを回収する
ans = 0
for i in range(4):
    for j in range(4):
        for k in range(4):
            ans += dp[N][i][j][k]
            ans %= MOD
print(ans)