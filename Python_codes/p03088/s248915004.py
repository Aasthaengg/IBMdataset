MOD = 10 ** 9 + 7
CHARS = 'ACGT'

def pos(ch):
    return CHARS.index(ch)

def ok(s):
    if 'AGC' in s:
        return False
    l = list(s)
    for i in range(len(s) - 1):
        l[i], l[i + 1] = l[i + 1], l[i]
        if 'AGC' in ''.join(l):
            return False
        l[i], l[i + 1] = l[i + 1], l[i]
    return True

n = int(input())
#dp[i][a][b][a] - number of ways to construct a correct string of length n, ending in abc characters
dp = [[[[0 for _ in range(4)] for _ in range(4)] for _ in range(4)] for _ in range(n + 1)]
for a in CHARS:
    for b in CHARS:
        for c in CHARS:
            if ok(a + b + c):
                dp[3][pos(a)][pos(b)][pos(c)] += 1
for i in range(4, n + 1):
    for a in CHARS:
        for b in CHARS:
            for c in CHARS:
                for d in CHARS:
                    if not ok(a + b + c + d):
                        continue
                    dp[i][pos(b)][pos(c)][pos(d)] += dp[i - 1][pos(a)][pos(b)][pos(c)]
                    dp[i][pos(b)][pos(c)][pos(d)] %= MOD
ret = 0
for a in CHARS:
    for b in CHARS:
        for c in CHARS:
            ret += dp[n][pos(a)][pos(b)][pos(c)]
            ret %= MOD
print(ret)
