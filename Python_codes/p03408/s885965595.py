from collections import defaultdict

N=int(input())
s=[input() for _ in range(N)]
M=int(input())
t=[input() for _ in range(M)]

x=defaultdict(int)
for i in s:
  x[i]+=1
  
for i in t:
  x[i]-=1
  
ans=0
for y in x.keys():
  ans=max(ans, x[y])
  
print(ans)