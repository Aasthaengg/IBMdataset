import re

def makelist(n, m):
    return [[0 for i in range(m)] for j in range(n)]

N = int(input())

MOD = int(1e9) + 7

acgt = ["A", "C", "G", "T"]
changed = [".*AGC", ".*GAC", ".*ACG", ".*A.GC", ".*AG.C"]
abcl = [ a+b+c for a in acgt for b in acgt for c in acgt]

dp = {}
for now in abcl:
    if any(map(lambda ch: re.match(ch, now), changed)):
        dp[now] = 0
    else:
        dp[now] = 1

N -= 3

while N > 0:
    dpNow = {}
    for abc in abcl:
        abc = abc[:min(N, 3)]
        dpNow[abc] = 0
        for key, value in dp.items():
            now = key + abc
            if not any(map(lambda ch: re.match(ch, now), changed)):
                dpNow[abc] += value
                dpNow[abc] %= MOD
    dp = dpNow
    N -= 3

ans = 0
for v in dp.values():
    ans += v
    ans %= MOD

print(ans)
