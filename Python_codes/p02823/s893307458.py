n,a,b=map(int,input().split())
if (a-b)%2:
    print(min(n-b+1+(b-1-a)//2,a-1+1+(b-a-1)//2))
else:
    print(abs(a-b)//2)