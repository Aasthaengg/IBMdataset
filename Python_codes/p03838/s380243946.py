x,y = map(int,input().split())
ans = 0
if x > y:
    if x >= 0 and y >= 0: # x,yが両方とも正
        if y == 0:
            print(x-y+1)
        else:
            print(x-y+2)
    elif x < 0 and y < 0: # x,yが両方とも負
        print(x-y+2)
    else:                 # xが正、yが負
        if x > -y:
            print(x+y+1)
        elif x < -y:
            print(-y-x+1)
        else:
            print(1)
else:                     # yの方が大きい
    if x >= 0 and y >= 0: # x,yが両方とも正
        print(y-x)
    elif x < 0 and y < 0: # x,yが両方とも負
        print(y-x)
    else:                 # xが負、yが正
        if -x > y:
            if y == 0:
                print(-x-y)
            else:
                print(-x - y + 1)
        elif -x < y:
            print(y+x+1)
        else:
            print(1)
