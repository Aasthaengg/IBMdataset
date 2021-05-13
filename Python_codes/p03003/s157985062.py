N,M = map(int, input().split())
S = list(map(int, input().split()))
T = list(map(int, input().split()))

# dp[i][j] : Sのi-1文字目、Tのj-1文字目までの解(文字目は0-index)
dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
#print(dp)
MOD = 10 ** 9 + 7

# なぜこれでよいのかわからない。。。
for i in range(1,N+1):
  for j in range(1,M+1):
    if S[i-1] == T[j-1]:
      # Sのi-1文字目、Tのj-1文字目が一致している場合は、
      # Sのi-2文字目、Tのj-2文字目までの部分列それぞれ
      # Sのi-1文字目、Tのj-1文字目を追加したものと、
      # Sのi-1文字目だけ、Tのj-1文字目だけの部分列パターンが
      # 増えるということだろうか。
      # つまり
      # dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + (dp[i-1][j-1] + 1)
      #            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      #            ここはS[i-1] != T[j-1]のときと同じ。
      # ということか？
      dp[i][j] = dp[i][j-1] + dp[i-1][j] + 1
    else:
      # dp[i-1][j-1]を引いているのは重複部分の排除？
      dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]
    #print(i,j,dp[i][j],dp[i][j-1],dp[i-1][j],dp[i-1][j-1])
    dp[i][j] %= MOD
print(dp[N][M]+1) #1を足しているのは部分列()の分をカウントするため？
