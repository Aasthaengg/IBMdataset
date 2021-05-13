n=int(input())
d={}
for x in range(n):
  s=int(input())
  if s in d:
    if d[s]==0:
      d[s]=1
    else:
      d[s]=0
      
  if s not in d:
    d[s]=1
  
ans=0
for y in d:
  if d[y]==1:
    ans+=1
    
print(ans)