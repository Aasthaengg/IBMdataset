N=int(input())
S=["".join(sorted(input())) for _ in range(N)]
d={}
ans=0
for s in S:
  if s in d:
    ans+=d[s]
    d[s]+=1
  else:
    d[s]=1
print(ans)