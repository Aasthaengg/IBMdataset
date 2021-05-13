n,k = map(int,input().split())
a = list(map(int,input().split()))

import collections
c = collections.Counter(a)

v,cts = zip(*c.most_common())
x = [int(i) for i in cts]
print(sum(x[k:]))