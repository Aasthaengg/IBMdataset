n,k=map(int,input().split())
x=list(map(int,input().split()))

xmin=(x[n-1]-x[0])*2

for i in range(n-k+1):
    x1=abs(x[i])+abs(x[i+k-1]-x[i])
    x2=abs(x[i+k-1])+abs(x[i+k-1]-x[i])
    xmin=min(xmin,x1,x2)

print(xmin)
