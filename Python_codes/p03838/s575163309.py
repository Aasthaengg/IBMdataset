x, y = map(int, input().split())

if y >= x:
    if x >= 0:
        print(y-x)
    elif y >= 0:
        if y >= abs(x):  
            print(min(y-x, y+x+1))
        else:
            print(min(-y-x+1, y-x))
    else:
        print(-x+y)
else:
    if y >= 0:
        print(min(x-y+2, y+x+1))
    elif x >= 0:
        if x >= abs(y):  
            print(min(x-y, x+y+1))
        else:
            print(-y-x+1)
    else:
        print(-y+x+2)
    
