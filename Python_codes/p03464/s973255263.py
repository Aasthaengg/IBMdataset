import math
k=int(input())
A=[int(i) for i in input().split()]
A=A[::-1]
u_lim,l_lim=2,2
ans=0
for i in range(k):
  a=A[i]
  if math.ceil(l_lim/a)>math.floor(u_lim/a):
    ans=-1
  l_lim=math.ceil(l_lim/a)*a
  u_lim=math.floor(u_lim/a)*a+a-1
if ans==-1:
  print(-1)
else:
  print(l_lim,u_lim)