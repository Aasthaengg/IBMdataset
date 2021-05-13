num = input().split()
if int(num[0])<int(num[1]):
    x = int(num[1])
    y = int(num[0])
else:
    x = int(num[0])
    y = int(num[1])

end = 0
    
z = x % y
if z == 0:
    print(y)
else:
    while True:
        z1 = y % z
        y1 = z
        if z1 == 0:
            print(z)
            break 
        z = z1
        y = y1    