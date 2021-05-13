x,y = map(int, input().split())
if abs(x) <= abs(y):
    c = abs(abs(x) - abs(y))
    if x >= 0 and y >= 0:
        print(c)
    elif x < 0 and y < 0:
        print(c+2)
    else:
        print(c+1)
else:
    c = abs(abs(x) - abs(y))
    if y == 0 and x < 0:
        print(c)
    elif y ==0 and x>=0:
        print(c+1)
    elif x >= 0 and y >= 0:
        print(c+2)
    elif x < 0 and y < 0:
        print(c)
    else:
        print(c+1)