n = int(input())
d = list(map(int,input().split()))

import itertools
e = itertools.combinations(list(range(n)),2)
ans = 0
for i,j in e:
  ans += d[i] * d[j]
print(ans)