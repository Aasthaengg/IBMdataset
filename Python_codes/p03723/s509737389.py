a,b,c=map(int,input().split())

if a%2==1 or b%2==1 or c%2==1:
  print(0)
  exit()
if a==b==c:
  print(-1)
  exit()
ans=0
while a%2==0 and b%2==0 and c%2==0:
    a,b,c=(b+c)//2,(c+a)//2,(a+b)//2
    ans+=1 
print(ans)