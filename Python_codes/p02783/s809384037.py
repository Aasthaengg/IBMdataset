n,d=list(map(int,input().split()))
if n%d==0:
    print(n//d)
else:
    print((n//d)+1)