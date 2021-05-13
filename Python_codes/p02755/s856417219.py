import math
N,M = map(int,input().split())
n = math.ceil(N/0.08)
m = int(M/0.1)
ans = 2000
if int(n*0.1) ==M:
  ans = min(n,ans)
if int(m*0.08) ==N:
  ans =min(m,ans)
  
if int(n*0.1)!=M and int(m*0.08)!=N:
  ans = -1
  
print(ans)