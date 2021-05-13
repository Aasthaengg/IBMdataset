
import collections
n = int(input())
s = list(input())

ans = 1
c = collections.Counter(s)
for i in set(s):
    ans *= (c[i] + 1)
print((ans - 1) % (pow(10, 9) + 7))
