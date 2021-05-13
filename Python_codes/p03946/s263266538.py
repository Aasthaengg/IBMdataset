n,t=map(int,input().split())
a=list(map(int,input().split()))
lmin=[a[0]]
rmax=[a[-1]]
for i in range(1,n):
  if a[i]<=lmin[-1]:
    lmin.append(a[i])
  else:
    lmin.append(lmin[-1])
  if a[-i-1]>=rmax[-1]:
    rmax.append(a[-i-1])
  else:
    rmax.append(rmax[-1])
mxls=[rmax[-i-2]-lmin[i] for i in range(n-1)]
mxls.append(-10**18)
ans=0
mx=max(mxls)
for i in range(n-1):
  if mxls[i]==mx and mxls[i]!=mxls[i+1]:
    ans+=1
print(ans)