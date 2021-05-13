X, Y = map(int, input().split())
if X % Y != 0:
    print(X)
elif X*2%Y != 0:
    print(X*2)
else:
    print(-1)