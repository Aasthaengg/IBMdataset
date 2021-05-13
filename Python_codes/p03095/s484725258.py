from collections import Counter

N = int(input())
S = input()
MOD = 10 ** 9 + 7
counter = Counter(S)
ans = 1
for e in counter.values():
    ans = ans * (e + 1) % MOD
print(ans - 1)
