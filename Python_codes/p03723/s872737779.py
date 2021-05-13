a,b,c=map(int,input().split())
if a==b==c and a%2==0:
    print(-1)
elif a==b==c and a%2==1:
    print(0)
    
else:
    cnt=0
    while a%2==b%2==c%2==0:
        total=a+b+c
        a=total//2-a//2
        b=total//2-b//2
        c=total//2-c//2
        cnt+=1
    print(cnt)