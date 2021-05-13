import collections
import sys
n = int(input())
a = list(map(int,input().split()))
if len(set(a)) == 1:
  print(n//2)
  sys.exit()
a1 = [a[x] for x in range(0,n,2)]
l_a1 = len(a1)
a2 = [a[y] for y in range(1,n,2)]
l_a2 = len(a2)
c1 = collections.Counter(a1)
c2 = collections.Counter(a2)
K_a1 = c1.most_common()[0][0]
K_a2 = c2.most_common()[0][0]
F_a1 = c1.most_common()[0][1]
F_a2 = c2.most_common()[0][1]
if K_a1 == K_a2:
  if  F_a1 > F_a2:
    F_a2 = c2.most_common()[1][1]
  elif F_a1 == F_a2:
    if  c1.most_common()[1][1] >  c2.most_common()[1][1]:
      F_a1 =  c1.most_common()[1][1]
    else:
      F_a2 =  c2.most_common()[1][1]
  else:
    F_a1 = c1.most_common()[1][1]
print((l_a1 - F_a1)+(l_a2 - F_a2))