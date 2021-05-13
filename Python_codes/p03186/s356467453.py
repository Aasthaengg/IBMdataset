a,b,c = map(int,input().split())
if (a+b) >= c:
    print(b+c)
else:
    print(min(b,c)*2+min(a,c)+1)