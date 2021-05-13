x,y = map(int,input().split())
ax = abs(x)
ay = abs(y)
if ax == ay and x != y:
    a = 1
elif x > y and 0 < y:
    a = ax - ay + 2
elif x > y and y == 0:
    a = ax - ay + 1
elif x > y and 0 > y:
    if ay > ax and x >= 0:
        a = ay - ax + 1
    elif ay > ax and x < 0:
        a = ay - ax + 2
    elif ax > ay:
        a = ax - ay + 1
elif y > x and x < 0 and ay > ax:
    a = ay - ax + 1
elif y > x and x < 0 and y > 0 and ax > ay:
    a = ax - ay + 1
else:
    a = y-x
print(a)