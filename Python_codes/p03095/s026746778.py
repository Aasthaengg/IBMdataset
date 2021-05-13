n = int(input())
s = input()
MOD = 10 ** 9 + 7

from collections import Counter

c = Counter(list(s))

res = 1
for v in c.values():
	res *= v + 1
	res %= MOD

print(res - 1)