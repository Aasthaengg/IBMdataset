a,b,c = list(map(int, input().split()))

if a==b==c:
    if a&1:
        print(0)
    else:
        print(-1)
    exit()

ans=0    
while all(i&1==0 for i in [a,b,c]):
    a,b,c = (b+c)//2, (a+c)//2, (a+b)//2
    ans+=1

print(ans)