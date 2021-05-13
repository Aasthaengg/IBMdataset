x, y = map(int, input().split())

if x >= 0 and y >= 0:
    if y > x:
        print(y-x)
    else:
        print(x+1)
elif x >= 0 and y < 0:
    if abs(y) < x:
        print(1+x-abs(y))
    else:
        print(1+abs(y)-x)
elif x < 0 and y >= 0:
    if abs(x) == y:
        print(1)
    elif abs(x) < y:
        print(1+y-abs(x))
    else:
        t1 = abs(x)+y
        t2 = abs(x)-y+1
        print(min(t1,t2))
else:
    if x < y:
        print(abs(x)-abs(y))
    else:
        print(1+abs(y)-abs(x)+1)