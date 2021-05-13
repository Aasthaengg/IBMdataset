x, y = map(int, input().split())
if x*y < 0 or x*y == 0 and x > y: print(abs(abs(x)-abs(y))+1)
elif x <= y: print(y-x)
else: print(x-y+2)