N=int(input())
s=[input() for _ in range(N)]
M=int(input())
t=[input() for _ in range(M)]
ans=-10**9
for i in range(N):
  a=0
  for j in range(N):
    if s[i]==s[j]:
      a+=1
  for k in range(M):
    if s[i]==t[k]:
      a-=1
  ans=max(ans,a)
if ans<0:
  print(0)
else:
  print(ans)