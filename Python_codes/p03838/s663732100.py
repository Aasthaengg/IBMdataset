x,y = map(int,input().split())
ch = max(abs(x),abs(y)) - min(abs(x),abs(y))
if x <= 0 and y == 0 or x == y or x == 0 and y > 0:
    print(ch)
elif x*y <= 0:
    print(ch+1)
elif x*y >= 0 and x >= y:
    print(ch+2)
else:
    print(ch)