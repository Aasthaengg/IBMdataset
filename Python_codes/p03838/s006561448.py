x,y = map(int,input().split())
if 0 <= x < y or x < y <= 0:
    print(abs(y-x))
elif 0 < y < x or y < x < 0:
    print(abs(x-y) + 2)
elif x < y:
    if y < abs(x):
        print(abs(x)-y + 1)
    else:
        print(y-abs(x) + 1)
else:
    if x < abs(y):
        print(abs(y)-x + 1)
    else:
        print(x-abs(y) + 1)