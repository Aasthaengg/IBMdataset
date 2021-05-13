n,a,b=map(int,input().split())
if (a+b)%2==0:
    print(abs(a-b)//2)
else:
    
    temp=min(b-1,n-a)
    if temp==b-1:
        ans=(b+a-1)//2
    else:
        
        ans=(n+1-b+n+1-a-1)//2
    print(ans)