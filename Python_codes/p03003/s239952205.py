def count_cs(str1, str2, MOD):
    """文字列str1, str2の共通部分列(Common Subsequence, CS)を数え上げる。
    添字が異なる場合は異なる部分列として考える。
    計算量 O(|str1||str2|)
    """
    dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
    for i in range(len(str1)):
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] + 1
            else:
                dp[i + 1][j + 1] = dp[i + 1][j] + dp[i][j + 1] - dp[i][j]
            dp[i + 1][j + 1] %= MOD
    return (dp[len(str1)][len(str2)] + 1) % MOD


n, m = map(int, input().split())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
MOD = 10 ** 9 + 7


print(count_cs(s, t, MOD))