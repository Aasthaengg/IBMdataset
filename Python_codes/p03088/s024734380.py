from collections import Counter


MOD = 10 ** 9 + 7


def isOK(last3, s):
    for i in range(len(last3 + s)):
        t = list(last3 + s)
        if i >= 1:
            t[i], t[i - 1] = t[i - 1], t[i]
        if ''.join(t).count('AGC'):
            return False
    return True


S = 'ACGT'
N = int(input())
dp = [None] * (N + 1)

dp[1] = Counter()
for s1 in S:
    dp[1][s1] += 1

dp[2] = Counter()
for s1 in S:
    for s2 in S:
        dp[2][s1 + s2] += dp[1][s1]

dp[3] = Counter()
for s1 in S:
    for s2 in S:
        for s3 in S:
            if isOK(s1 + s2, s3):
                dp[3][s1 + s2 + s3] += dp[2][s1 + s2]

for i in range(4, N + 1):
    dp[i] = Counter()
    for s1 in S:
        for s2 in S:
            for s3 in S:
                for s4 in S:
                    if isOK(s1 + s2 + s3, s4):
                        dp[i][s2 + s3 + s4] += dp[i - 1][s1 + s2 + s3]
                        dp[i][s2 + s3 + s4] %= MOD

print(sum(dp[N].values()) % MOD)
