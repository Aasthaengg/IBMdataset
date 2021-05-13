n,k=map(int,input().split())
x=0
y=0
for i in range(1,n+1):
    if i%k==0:
        x+=1
    if i%k==k//2:
        y+=1
ans=x**3
if k%2==0:
    ans+=y**3
print(ans)