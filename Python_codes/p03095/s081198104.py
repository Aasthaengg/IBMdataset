n = int(input())
s = input()
import collections
c = collections.Counter(s)
res = 1
m = 10 ** 9 + 7
for k in c:
    res *= (c[k] + 1)
    res %= m
res -= 1
res %= m
print(res)
