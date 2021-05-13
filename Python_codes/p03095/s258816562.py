n = int(input())
s = list(input())
import collections
c = collections.Counter(s)
lis = list(c.values())
ans = 1
for A in lis:
    ans *= A + 1
print((ans-1)%1000000007)