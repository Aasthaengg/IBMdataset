import numpy as np
import sys
N, M = [int(x) for x in input().split()]
s = []
c = []
for i in range(M):
  a, b = [int(x) for x in input().split()]
  s.append(a)
  c.append(b)
  
ans = np.full(N+1, -1)
for i in range(M):
  if(ans[s[i]]==-1):
    ans[s[i]] = c[i]
  elif(ans[s[i]]!=c[i]):
    print(-1)
    sys.exit()
if(ans[1]==-1)and(N>1):
  ans[1] = 1
ans = np.where(ans==-1, 0, ans)
 
if(ans[1]==0)and(N!=1):
  print(-1)
  sys.exit()
Ans = 0
for i in range(1, N+1):
  Ans += 10**(N-i)*ans[i]
print(int(Ans))