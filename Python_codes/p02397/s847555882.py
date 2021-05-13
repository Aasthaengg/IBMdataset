for i in range(1,3001):
    x, y = [int(i) for i in input().split()]
    if x + y == 0:
        break
    elif x>y:
        print(y,x)
    elif x<y:
        print(x,y)
    else:
        print(x,y)