x,y = [int(x) for x in input().split()]
 
if y == 0:
    print(abs(x) + (x>0))
elif x < y < 0:
    print(y-x)
elif 0 < y < x:
    print(x-y+2)
else:
    print(abs(abs(y) - abs(x)) + (x < 0) + (y < 0))