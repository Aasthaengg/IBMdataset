x, y = map(int,input().split())

if x >= 3 and y >= 3:
    print((x-2)*(y-2))
elif x == 2 or y == 2:
    print(0)
elif x == 1 and y == 1:
    print(1)
else:
    print(max(x,y)-2)