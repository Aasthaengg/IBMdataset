S = input()

# dp[i][n] := i文字目までのNONE,A,AB,ABCを決めた数
dp = [[0]*4 for i in range(len(S)+1)]
NO, A, AB, ABC = 0, 1, 2, 3
MOD = 10**9+7
dp[0][NO] = 1
for i in range(len(S)):
    # カウントを進めない時
    for j in range(4):
        if S[i] == "?":
            dp[i+1][j] += dp[i][j]*3
        else:
            dp[i+1][j] += dp[i][j]
    # それ以外
    if S[i] == "A" or S[i] == "?":
        dp[i+1][A] += dp[i][NO]
    if S[i] == "B" or S[i] == "?":
        dp[i+1][AB] += dp[i][A]
    if S[i] == "C" or S[i] == "?":
        dp[i+1][ABC] += dp[i][AB]
    for j in range(4):
        dp[i+1][j] %= MOD
    
print(dp[len(S)][ABC])


    
