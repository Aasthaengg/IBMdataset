W,H,N = list(map(int,input().split()))

X = [0,W]
Y = [0,H]

for n in range(N):
    x,y,a = list(map(int,input().split()))
    if a == 1:
        X[0] = max(X[0],x)
    elif a == 2:
        X[1] = min(X[1],x)
    elif a == 3:
        Y[0] = max(Y[0],y)
    elif a == 4:
        Y[1] = min(Y[1],y)
    
# print((X[1]-X[0])*(Y[1]-Y[0]))
print(max(0,X[1]-X[0])*max(0,Y[1]-Y[0]))