x,y = map(int,input().split())
if ((x >= 0 and y >= 0) or (x < 0 and y < 0)) and x < y:
    print(abs(x-y))
elif (x >= 0 and y >= 0) and y < x:
    print(abs(x-y+1+(y != 0)))
elif (x < 0 and y < 0) and y < x:
    print(abs(x-y)+2)
elif x == -y:
    print(1)
else:
    print(abs(abs(x)-abs(y))+(y != 0))