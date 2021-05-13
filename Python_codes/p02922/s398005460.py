a,b=map(int,input().split())
ans=0
for i in range(1,b,a-1):
  ans+=1
print(ans)