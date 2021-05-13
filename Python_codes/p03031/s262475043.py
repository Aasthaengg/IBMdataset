n,m=map(int,input().split())
S=[]
for _ in range(m):
  s=list(map(int,input().split()))
  S.append(s[1:])
p=list(map(int,input().split()))

ans=0
for i in range(1<<n):
  for k in range(m):
    sw=0
    for j in range(n):
      if (i>>j)&1 and j+1 in S[k]:
        sw+=1
    if sw % 2 != p[k]:
      break
  else:
    ans+=1
print(ans)

