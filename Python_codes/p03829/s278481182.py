n,a,b=map(int,input().split())
x=list(map(int,input().split()))

tired=0
for i in range(n-1):
    if a*(x[i+1]-x[i])<=b:
        tired+=a*(x[i+1]-x[i])
    else:
        tired+=b
print(tired)