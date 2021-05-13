"""
?AGC
AG?C
A?GC
?ACG
?CAG
"""

n = int(input())

# dp i文字目までのパターン　前の3文字を保存する
import itertools
l = ["A", "G", "C", "T"]
pl = itertools.product(l, repeat=3)

dic = dict()
dic2 = dict()
from collections import defaultdict
ng_list = defaultdict(int)


for idx, p in enumerate(pl):
    dic[idx] = p
    dic2[p] = idx

pl = itertools.product(l, repeat=4)
for idx, p in enumerate(pl):
    if p[1] == "A" and p[2] == "G" and p[3] == "C":
        ng_list[p] = 1
    elif p[0] == "A" and p[1] == "G" and p[3] == "C":
        ng_list[p] = 1
    elif p[1] == "A" and p[2] == "C" and p[3] == "G":
        ng_list[p] = 1
    elif p[1] == "G" and p[2] == "A" and p[3] == "C":
        ng_list[p] = 1
    elif p[0] == "A" and p[2] == "G" and p[3] == "C":
        ng_list[p] = 1

pl = itertools.product(l, repeat=3)
dic3 = dict()
dic4 = dict()
for idx, p in enumerate(pl):
    dic3[idx] = p
    dic4[p] = idx

dp = [[0 for _ in range(4**3)] for _ in range(n+1)]
dp[0][dic4[("T", "T", "T")]] = 1
MOD = 10 ** 9 + 7
for i in range(n):
    for j in range(4**3):
        for k in l:
            if ng_list[dic3[j] + (k,)] == 0:
                dp[i+1][dic4[dic3[j][1:] + (k,)]] += dp[i][j]
                dp[i+1][dic4[dic3[j][1:] + (k,)]] %= MOD

print(sum(dp[-1]) % MOD)

