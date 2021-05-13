a,b=map(int,input().split())
ans=0
for i in range(0,100):
  for j in range(0,10):
    x=int(str(i)+str(j)+str(i)[::-1])
    if(a<=x and x<=b):
      ans+=1
    
print(ans)