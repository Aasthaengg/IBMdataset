a,b,c=map(int,input().split())

if a+b>=c:
    print(c+b)
elif a+b<c:
    print(a+b+1+b)