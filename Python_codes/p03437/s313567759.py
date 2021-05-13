X, Y = map(int, input().split())
num = 0
if X % Y == 0:
    print(-1)
else:
    while True:
        num += X
        if X % Y != 0:
            print(num)
            break
