n=int(input())
s=list(input())

import collections
c=collections.Counter(s)
c=c.most_common()

ans=1
for i in range(len(c)):
    ans *= (c[i][1]+1)
print((ans-1)%(10**9+7))