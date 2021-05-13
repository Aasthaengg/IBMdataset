import itertools
n,m,x=map(int, input().split())
a = [list(map(int, input().split())) for l in range(n)]
bit=list(itertools.product([0,1],repeat=n))
M=10**7
for i in range(2**n):
  cnt1=[0]*m
  cnt2=0
  for j in range(n):
    if bit[i][j]==1:
      cnt2+=a[j][0]
      for k in range(m):
        cnt1[k]+=a[j][k+1]
  ans=True
  for j in range(m):
    if cnt1[j]<x:
      ans=False
  if ans:
    M=min(cnt2,M)
if M==10**7:
  print(-1)
else:
  print(M)