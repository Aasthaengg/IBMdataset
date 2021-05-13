x, y = map(int, input().split())

if y == 0:
    if x >= 0:
        print(x+1)
    else:
        print(-x)
    exit()

if x >= 0 and y >= 0:
    if x <= y:
        print(y-x)
    else:
        print(1+(-y+x)+1)
elif x >= 0 and y <= 0:
    if x >= -y:
        print(1+x-(-y))
    else:
        print(-y-x+1)
elif x <= 0 and y >= 0:
    if y >= -x:
        print(1+(y-(-x)))
    else:
        print(-y-x+1)
else:
    if x <= y:
        print(y-x)
    else:
        print(1-y+x+1)
