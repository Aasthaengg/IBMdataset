n,k=map(int,input().split())
a=[]
for _ in range(n):
  x,y=map(int,input().split())
  d=[x,y]
  a.append(d)
  
a.sort()
ans=0
ans1=0

for d in a:
  if (ans+d[1])>=k:
    ans1=d[0]
    break
    
  else:
    ans+=d[1]
    
print(ans1)
