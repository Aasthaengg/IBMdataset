from itertools import *
A,B,C = map(int,input().split())
ans = 10**18
if A%2 == 0 or B%2 == 0 or C%2 == 0:
  ans = 0
else:
  for i,j in combinations([A,B,C],2):
    ans = min(ans,i*j)
print(ans)