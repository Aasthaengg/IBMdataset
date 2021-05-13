N = int(input())
S = input()
import collections
MOD = 10 ** 9 + 7

dct = dict(collections.Counter(S))

ans = 1
for val in dct.values():
    ans = (ans * (val + 1)) % MOD
print(ans - 1)