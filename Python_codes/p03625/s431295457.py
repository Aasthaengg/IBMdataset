N = int(input())
A = list(map(int, input().split()))

import collections
ans = 0
c = collections.Counter(A)
lis = []
for k,v in c.items():
  if v>=2:
    lis.append(k)
  if v>=4:
    lis.append(k)
if len(lis)>=2:
  lis.sort()
  ans = lis[-1]*lis[-2]
print(ans)

#print(*ans, sep='\n')
