a , b , k = map(int,input().split())

if k % 2 == 0:
    for i in range(int(k / 2)):
        if a % 2 == 1:
            a -= 1
        a = a / 2
        b += a
        if b % 2 == 1:
            b -= 1
        b = b / 2
        a += b
else:
    for i in range(int((k - 1) / 2)):
        if a % 2 == 1:
            a -= 1
        a = a / 2
        b += a
        if b % 2 == 1:
            b -= 1
        b = b / 2
        a += b
    if a % 2 == 1:
        a -= 1
    a = a / 2
    b += a
    
print(int(a),end=" ")
print(int(b))