N,M,X,Y = list(map(int,input().split()))
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x.append(X)
y.append(Y)
maxX = max(x)
minY = min(y)
if maxX < minY:
    print("No War")
else:
    print("War")