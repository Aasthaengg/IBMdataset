X, Y = map(int, input().split())
if X % Y == 0:
    print(-1)
else:
    n = 1
    while True:
        if X*n % Y != 0:
            print(X*n)
            break
        else:
            n += 1