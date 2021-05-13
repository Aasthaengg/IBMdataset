X,Y=map(int,input().split())
if Y<X:
    print(0)
else:
    count=1
    while X<Y:
        X*=2
        if X<=Y:
            count+=1
    print(count)