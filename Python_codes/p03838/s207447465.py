x, y = list(map(int, input().split()))

dif = abs(abs(x)-abs(y))

if (x >= 0 and y > 0) or (x < 0 and y <= 0):
    if x < y:
        print(dif)
    else:
        print(dif + 2)
else:
    print(dif + 1)