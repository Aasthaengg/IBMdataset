X,Y = map(int, input().split())

if X%Y == 0:
    print(-1)
else:
    i = 1
    while 1:
        if X*i > 10**18:
            print(-1)
            break
        elif X*i%Y!=0:
            print(X*i)
            break
        else:
            i+= 1