n,m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
x = [0]
mod = m
for i in range(n):
    x.append((a[i]+x[i])%mod)
ans = 0
from collections import Counter
c = dict(Counter(x))
for i in c.values():
    ans += i*(i-1)//2
print(ans)