k,s=map(int,input().split())
ans=0
for x in range(k+1):
  for r in range(s-k,s+1):
    if r-x<0:
      continue
    if r-x>k:
      continue
    ans+=1
      
print(ans)