n,k=map(int,input().split())
v=list(map(int,input().split()))
finans=0
for l in range(n+1):
  for r in range(n-l+1):
    if l+r>k:
      continue
    ans=[]
    for i in range(l):
      ans.append(v[i])
    for i in range(n-1,n-r-1,-1):
      ans.append(v[i])
    ans.sort()
    i=-1
    for i in range(min(len(ans),k-(r+l))):
      if ans[i]>0:
        i-=1
        break
    ans1=0
    for j in range(i+1,len(ans)):
      ans1+=ans[j]
    finans=max(finans,ans1)
print(finans)