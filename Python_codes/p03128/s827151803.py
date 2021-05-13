N, M = [int(x) for x in input().split()]
A = [int(x) for x in input().split()]

# argsは数を文字列で表したリスト
# 一番大きい数を文字列として出力
def maxnum(*args):
    maxn = args[0]
    for i in range(1, len(args)):
        if len(maxn) != len(args[i]):
            if len(args[i]) > len(maxn):
                maxn = args[i]
        else:
            maxn = max(maxn, args[i])
    return maxn


# 数字0〜9を作るのに必要なマッチ棒の数
nmatch = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

dp = [""] + [None] * N
for i in range(1, N + 1):
    maxn = ""
    for a in A:
        if i - nmatch[a] >= 0 and dp[i - nmatch[a]] != None:
            maxn = maxnum(maxn, dp[i - nmatch[a]] + str(a), str(a) + dp[i - nmatch[a]])
            dp[i] = maxn

print(dp[N])
