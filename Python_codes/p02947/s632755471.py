N=int(input())
S=[''.join(sorted(input())) for _ in range(N)]
ans=0
import collections
from math import factorial
c = collections.Counter(S)
for i in c.values():
    if 2<=i:
        ans+=factorial(i)//(factorial(i-2)*factorial(2))

print(ans)