N,Y = map(int,input().split())
x = y = z = 0
while  Y >= 10000:
    x += 1
    N -= 1
    Y -= 10000
while Y >= 5000:
    y += 1
    N -= 1
    Y -= 5000
while Y >= 1000:
    z += 1
    N -= 1
    Y -= 1000
if Y != 0 or N < 0:
    x = y = z = -1
else:
    while N >= 9 and x > 0:
        x -= 1
        z += 10
        N -= 9
    while N >= 4 and y > 0:
        y -= 1
        z += 5
        N -= 4
    while N > 0 and x > 0:
        x -= 1
        y += 2
        N -= 1
    if N != 0:
        x = y = z = -1
print(x,y,z)