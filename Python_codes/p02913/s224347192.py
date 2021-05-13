# who says a pun?

# 今日の精進問題第三問目ｎ

n = int(input())
s = list(input())
# dp[L][K]=一番目は左からL番目、二番目は左からK番目からスタートするとした時の共通文字列の中で長さが最大のもの
dp = [[0 for i in range(n + 2)] for j in range(n + 2)]
# もしi>=jであるならば答えは当然ゼロ
# 0<i<jである時だけで考える
for j in range(n, 1, -1):
    # j=n,n-1,,,,,,,,2の値をとる
    for i in range(1, j):

        if s[i - 1] == s[j - 1]:
            dp[i][j] = dp[i + 1][j + 1] + 1
        else:
            dp[i][j] = 0
ans = 0
for j in range(2, n + 1):
    for i in range(1, j):
        ans = max(ans, min(dp[i][j],j-i))
print(ans)
