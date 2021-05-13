N=int(input())
p=list(map(int,input().split()))
q=sorted(p)
ans=0
for x in range(N):
  if p[x]!=q[x]:
    ans+=1
if ans==2 or ans==0:
  print("YES")
else:
  print("NO")