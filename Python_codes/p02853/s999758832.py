x,y = map(int,input().split())

z = 0

if x == 1 and y == 1:
    print(1000000)
    exit()

if  x == 1:
    z += 300000
elif x == 2:
    z += 200000
elif x == 3:
    z += 100000

if  y == 1:
    z += 300000
elif y == 2:
    z += 200000
elif y == 3:
    z += 100000

print(z)
