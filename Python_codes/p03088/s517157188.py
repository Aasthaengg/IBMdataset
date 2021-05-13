import re

def makelist(n, m):
    return [[0 for i in range(m)] for j in range(n)]

N = int(input())

acgt = ["A", "C", "G", "T"]
changed = [".*GAC.*", ".*ACG.*", ".*A.GC.*", ".*AG.C.*"]
bad = ".*AGC"


# initialize
dp = {}
for a in acgt:
    for b in acgt:
        for c in acgt:
            now = a+b+c
            
            if re.match(bad, now):
                dp[now] = 0
            elif any(map(lambda ch: re.match(ch, now), changed)):
                dp[now] = 0
            else:
                dp[now] = 1

N -= 3

MOD = int(1e9) + 7
# main
while N > 0:
    dpNow = {}
    for a in acgt:
        for b in acgt:
            for c in acgt:
                abc = (a + b + c)[:min(N, 3)]
                dpNow[abc] = 0
                for key, value in dp.items():
                    now = key + abc

                    if re.match(bad, now):
                        ()
                    elif any(map(lambda ch: re.match(ch, now), changed)):
                        ()
                    else:
                        dpNow[abc] += value
                        dpNow[abc] %= MOD
                        
    dp = dpNow
    N -= 3

ans = 0
for v in dp.values():
    ans += v
    ans %= MOD

print(ans)
