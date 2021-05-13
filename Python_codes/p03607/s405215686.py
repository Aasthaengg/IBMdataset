n = int(input())

a = [int(input()) for i in range(n)]

import collections
c = collections.Counter(a)

res = 0
for i in c:
  if c[i] % 2 != 0:
    res += 1
print(res)