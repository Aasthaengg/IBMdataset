X,Y=map(int,input().split())

if X>=0:
    if Y>=X:
        print(Y-X)
    elif -X<=Y<=0:
        print(Y-(-X)+1)
    elif 0<Y<X:
        print(X-Y+2)
    else:
        print(-Y-X+1)
else:
    if Y>=abs(X):
        print(Y-(-X)+1)
    elif X<=Y<=0:
        print(Y-X)
    elif 0<Y<abs(X):
        print(abs(X)-Y+1)
    else:
        print(abs(Y)-abs(X)+2)