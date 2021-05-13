x, y = map(int, input().split())
if y == 0:
    if x <= 0:
        print(abs(x))
    else:
        print(abs(x)+1)
elif x==0:
    if y < 0:
        print(-y+1)
    else:
        print(y)
elif x*y < 0:
    r = []
    x, y = sorted([x, y])
    r.append(abs(y-x))
    r.append(abs(y+x)+1)
    print(min(r))
elif x > y:
    print(abs(y-x)+2)
else:
    print(abs(y-x))