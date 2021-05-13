from collections import Counter
from functools import reduce
MOD = 10 ** 9 + 7

n = int(input())
s = input()

c = Counter(s)

ans = reduce(lambda total, x: total * (x+1) % MOD, c.values(), 1)

print(ans-1)