X, Y = map(int,input().split())
if Y % 2 == 0:
    if X <= (Y / 2) and (Y / 2) <= (2 * X):
        print("Yes")
    else:
        print("No")
else:
    print("No")