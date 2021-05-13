n,x=map(int,input().split())
a=list(map(int,input().split()))
ans=0

a.sort()

for i in a:
  x-=i
  if x>0:
    ans+=1
    continue
  
  elif x==0:
    ans+=1
    break
    
  else:
    break
    
if ans==n:
  if x!=0:
    ans-=1


print(ans)
