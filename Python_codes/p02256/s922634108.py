def euclidean_alg(x,y):
    while y:
        x,y=y,x%y
    return x

XY=list(map(int,input().split()))
x=max(XY)
y=min(XY)

print(euclidean_alg(x,y))