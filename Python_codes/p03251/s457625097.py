N,M,X,Y = map(int,input().split())
x = list(map(int,input().split()))
x.sort()
y = list(map(int,input().split()))
y.sort()
if max(X,x[-1]) < min(Y,y[0]):
    print("No War")
else:
    print("War")