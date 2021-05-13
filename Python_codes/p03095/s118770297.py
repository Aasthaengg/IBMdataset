n = int(input())
s = input()

MOD = 10**9 + 7

from collections import Counter

ctr = Counter(s)

ans = 1
for v in ctr.values():
    ans *= v + 1
    ans %= MOD
ans -= 1
ans %= MOD
print(ans)