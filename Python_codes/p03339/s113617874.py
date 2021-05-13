n=int(input())
s=list(input())
t=[]
for i in s:
  if i=="W":
    t.append(1)
  else:
    t.append(0)

from itertools import accumulate
t=[0]+list(accumulate(t))
ans=float("INF")
for i in range(1,n+1):
  ans=min(ans,t[i-1]+n-i-(t[n]-t[i]))

print(ans)
