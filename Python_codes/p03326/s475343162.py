n,m=map(int,input().split())
xyz=[list(map(int,input().split())) for i in range(n)]
ans=-10**18
tmp=[1,-1]
for i in range(2):
  for j in range(2):
    for k in range(2):
      xyz.sort(key=lambda x:x[0]*tmp[i]+x[1]*tmp[j]+x[2]*tmp[k],reverse=True)
      foo=sum([x[0]*tmp[i]+x[1]*tmp[j]+x[2]*tmp[k] for x in xyz][:m])
      ans=max(ans,foo)
print(ans)