x, y = sorted([int(i) for i in input().split()])
while x > 0:
    z = x
    x = y % x
    y = z
    
print(y)