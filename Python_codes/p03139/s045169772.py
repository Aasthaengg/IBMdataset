n,a,b=map(int,input().split())
total=a+b
if n==a==b:
    print(n,n)
    exit()
if n<total:
    print(min(a,b),total-n)
else:
    print(min(a,b),0)
