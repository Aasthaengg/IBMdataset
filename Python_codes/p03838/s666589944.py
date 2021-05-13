x,y = map(int, input().split())
if x < 0 and y < 0:
    if abs(x) < abs(y):
        print(abs(x-y)+2)
    else:
        print(abs(x-y))
elif x > 0 and y > 0:
    if abs(x) > abs(y):
        print(x-y+2)
    else:
        print(y-x)

elif x < 0 and y > 0:
    print(abs(y+x)+1)
elif x > 0 and y < 0:
    print(abs(y+x)+1)
elif x > 0 and y == 0:
    print(x+1)
elif x < 0 and y == 0:
    print(-x)
elif x == 0 and y == 0:
    print(0)
elif x == 0 and y < 0:
    print(-y + 1)
elif x == 0 and y > 0:
    print(y) 


