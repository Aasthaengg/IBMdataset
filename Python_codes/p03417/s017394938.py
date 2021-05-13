x,y = map(int,input().split())

if x == 1 and y == 1:
    print(1)
elif x == 1 and y != 1:
    print(y-2)
elif y == 1 and x != 1:
    print(x-2)
else:
    print((x-2)*(y-2))