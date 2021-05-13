a,b,c=map(int,input().split())

if b>=c:
    print(b+c)
else:
    print(b*2+min(a+1,c-b))
