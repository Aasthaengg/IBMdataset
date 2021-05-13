N,M,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
xr = max(x)
yl = min(y)

for i in range(X+1,Y+1):
    if(xr < i <= yl):
        print('No War')
        exit()

print('War')