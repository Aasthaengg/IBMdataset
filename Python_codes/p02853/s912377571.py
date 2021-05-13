X, Y = map(int, input().split())
s = [300000, 200000, 100000]
if X == 1 and Y == 1:
    print(s[0]*2 + 400000)
else:
    if X <= 3 and Y <= 3:
        print(s[X-1] + s[Y-1])
    elif X <= 3 and Y > 3:
        print(s[X-1])
    elif X > 3 and Y <= 3:
        print(s[Y-1])
    else:
        print(0)