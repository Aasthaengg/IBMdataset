x,y = map(int, input().split())
if x == y :
    print(0)
elif (-x) == y:
    print(1)
elif x >= 0 and x < y: # 0 1
    print(y-x)
elif x >= 0 and x > y: # 5 4 5 -7
    if x <= (-y): #10 -11
        print(abs(x-(-y))+1)
    else: # 10 -9
        print(min(abs(y-(-x))+1,abs(x-y)+2))
elif x < 0 and x > y: # -1 -3
    print(min(abs(x-y)+2, -y -x+1))
elif x < 0 and x < y: # -3 -1
    if y > 0: # -5 6
        print(min(abs(y-x),abs((-y)-x)+1))
    else:
        print(abs(y - x))

