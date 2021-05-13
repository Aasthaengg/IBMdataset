import math
N,D=map(int,input().split())
ans=0
for _ in range(N):
  p,q=map(int,input().split())
  if math.sqrt(p**2+q**2)<=D:
    ans+=1
print(ans)