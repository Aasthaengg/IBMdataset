


S = input()
N = len(S)
MOD = 10**9 + 7

# dp[i+1][j] : 左からi番目の文字まで見たときに、13で割ってj余る場合の数
dp = [[0 for _ in range(13)] for _ in range(N+1)]
dp[0][0] = 1


"""
数字がabcで並んでいて、それを13で割った時の余りがpのときに、末尾にdが追加されると、
abcd = abc * 10 + d だから、これを13で割った余りは、 p*10 % 13 + d % 13 = (10 * p + d) % 13

"""

for i in range(N):
    for j in range(13):
        if S[i] == "?":
            # 0~9
            for n in range(10):
                dp[i+1][(10 * j + n) % 13] += dp[i][j]
                if dp[i+1][(10 * j + n) % 13] >= MOD:
                    dp[i+1][(10 * j + n) % 13] %= MOD
        else:
            dp[i+1][(10 * j + int(S[i])) % 13] += dp[i][j]
            if dp[i+1][(10 * j + int(S[i])) % 13] >= MOD:
                dp[i+1][(10 * j + int(S[i])) % 13] %= MOD


print(dp[-1][5])

