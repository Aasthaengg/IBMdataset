n,a,b=map(int,input().split())
if a>b:
    print(0)
elif a==b:
    print(1)
elif n==1:
    print(0)
else:    
    print(n*b-b+a-n*a+a-b+1)