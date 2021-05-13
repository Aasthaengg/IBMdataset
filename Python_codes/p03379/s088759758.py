from bisect import *

n=int(input())
x=list(map(int,input().split()))
x_s=sorted(x)

ans1=x_s[n//2]
ans2=x_s[n//2-1]

for i in range(n):
  inx=bisect_right(x_s,x[i])
  if inx<=n//2:
    print(ans1)
  else:
    print(ans2)