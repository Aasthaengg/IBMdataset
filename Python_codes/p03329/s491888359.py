N=int(input())
inf=float("inf")

X=[inf]*(N+1)
X[0]=0

for x in range(1,N+1):
    X[x]=X[x-1]+1

    b=6
    while x>=b:
        X[x]=min(X[x],X[x-b]+1)
        b*=6

    c=9
    while x>=c:
        X[x]=min(X[x],X[x-c]+1)
        c*=9

print(X[-1])
