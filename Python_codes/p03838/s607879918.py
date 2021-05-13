X,Y = list(map(int,input().split()))

if X==Y:
    print(0)
if X<Y:
    if X<0 and Y>0:
        print(1+abs(Y+X))
    else:
        print(Y-X)

if X>Y:
    if X>=0 and Y<=0:
        print(1+abs(X+Y))
    elif X>0 and Y>0:
        print(2+X-Y)
    elif X<0 and Y<0:
        print(2+X-Y)
    else:
        print(X-Y)