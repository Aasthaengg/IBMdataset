X, Y = map(int, input().split(' '))
if X % Y == 0: print(-1)
else:
    res = 0
    i = 1
    while res == 0:
        if X * i % Y != 0:
            res = X*i
            break
        else:
            i += 1
    if X*i <= 10**18:
        print(res)
    else:
        print(-1)