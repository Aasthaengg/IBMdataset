X, Y = map(int, input().split())
i = X * 2
while True:
    if i > pow(10, 18) or X % Y == 0:
        print(-1)
        break
    if i % Y != 0:
        print(i)
        break
    i += X
