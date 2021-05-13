n=int(input())
ta=[list(map(int,input().split())) for _ in range(n)]
ans=ta[0]
for i in range(1,n):
  if (ta[i-1][0]<=ta[i][0]) and (ta[i-1][1]<=ta[i][1]):
    pass
  else:
    l=ta[i-1][0]//ta[i][0]
    if ta[i-1][0]%ta[i][0]!=0:
      l+=1
    r=ta[i-1][1]//ta[i][1]
    if ta[i-1][1]%ta[i][1]!=0:
      r+=1
    ta[i][0]*=max(l,r)
    ta[i][1]*=max(l,r)
print(sum(ta[-1]))