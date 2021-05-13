N=int(input())
S=[input() for i in range(N)]
BA=0
B=0
A=0
cnt=0
for i in S:
  if i[0]=='B'and i[-1]=='A':
    BA+=1
  elif i[0]=='B':
    B+=1
  elif i[-1]=='A':
    A+=1
  for j in range(len(i)-1):
    if i[j]=='A' and i[j+1]=='B':
      cnt+=1
if BA==0:
  print(cnt+min(A,B))
else:
  ans=BA-1
  if B>0:
    ans+=1
    B-=1
  if A>0:
    ans+=1
    A-=1
  print(cnt+min(A,B)+ans)