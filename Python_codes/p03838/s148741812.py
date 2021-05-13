x,y = map(int,input().split())
if abs(x)<=abs(y):
    count = 0
    if x <0:
        count += 1
    if y <0:
        count += 1
    count += abs(y)-abs(x)
    print(count)
else:
    if x <=0:
        a = y -x
        b = abs(x)-abs(y)+1
        print(min(a,b))
    else:
        a = 1 + (y+x)
        b = 1 + abs(x) - abs(y)
        if y > 0:
            b+= 1
        print(min(a,b))