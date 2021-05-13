n = int(input())

dp = [0 for _ in range(n+1)]

for i in range(1, n+1): # 1円の場合からn円の場合まで繰り返す
    Min = dp[i-1] + 1 # i-1円を引き出してから1円を引き出す場合の引き出し回数の最小値
    j = 1
    while pow(6, j) <= i:
        Min = min(Min, dp[i-pow(6, j)] + 1) # i-6^j円を引き出してから6^j円を引き出す場合の引き出し回数の最小値
        j += 1
    j = 1
    while pow(9, j) <= i:
        Min = min(Min, dp[i-pow(9, j)] + 1) # i-9^j円を引き出してから9^j円を引き出す場合の引き出し回数の最小値
        j += 1
    dp[i] = Min

print(dp[n])