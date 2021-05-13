from collections import Counter

n = int(input())
s = input()
MOD = 10**9 + 7

cnt = Counter(list(s))
ans = 1
for v in cnt.values():
    ans *= v + 1
    ans %= MOD
print(ans - 1)
