X,Y  = map(int, input().split())
if X > Y:
    if X % Y == 0:print(-1)
    else:print(X)
elif X == Y:
    print(-1)
else:
    print(X)