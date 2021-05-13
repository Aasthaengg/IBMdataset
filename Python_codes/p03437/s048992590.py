x, y = map(int, input().split(" "))
X = x
if x % y == 0:
    print(-1)
else:
    while X < 10 ** 18:
        if X % y != 0:
            print(X)
            exit()
        X = X + x
