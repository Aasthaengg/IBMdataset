a,b,c=map(int,input().split())
if a==b==c and a%2==0:
    print(-1)
    exit()
ans=0
while a%2==b%2==c%2==0:
    x=(a+b)//2
    y=(b+c)//2
    z=(c+a)//2
    a=y
    b=z
    c=a
    ans+=1
print(ans)