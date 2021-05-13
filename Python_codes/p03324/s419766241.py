d,n=map(int,input().split())

ans=1
for i in range(d):
    ans*=100
ans*=n

if d==0 and n==100:
    ans+=1
if d==1 and n==100:
    ans+=100
if d==2 and n==100:
    ans+=10000

print(ans)
