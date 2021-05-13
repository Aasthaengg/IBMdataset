n,a,b= map(int, input().split())

if (b-a)%2==0:
    print((b-a)//2)

elif b-a==1:
    print(min(b-1,n-a))

else:
    x=-(-(b-a)//2)
    print(min(x+a-1,x+n-b))