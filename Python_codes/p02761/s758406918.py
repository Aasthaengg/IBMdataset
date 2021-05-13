N,M=map(int,input().split())
p=True
l=[-1 for _ in range(N)]
for i in range(M):
  s,c=map(int,input().split())
  if l[s-1] == -1:
    l[s-1] = c
  elif not l[s-1]==c:
    p=False
if p:
  ans=""
  if len(l) == 1:
    if l[0] == -1:
      ans = "0"
    else:
      ans = str(l[0])
  elif l[0]==0:
    p=False
  elif l[0]==-1:
    ans="1"
  else:
    ans=str(l[0])
  for i in l[1:]:
    if i == -1:
      ans+="0"
    else:
      ans+=str(i)
print(int(ans) if p else -1)