x, y = map(int, input().split())
count = abs(abs(x) - abs(y))

if x*y >= 0 and y > x:
    print(y - x)
elif (0<y and 0<x) or (0>x and 0>y):
    print(count+2)
else:
    print(count+1)