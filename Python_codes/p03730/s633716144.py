a,b,c = map(int,input().split())
d = a * b
e = a

while e <= d:
    if e % b == c:
        break
    else:
        e += a

if e > d:
    print('NO')
else:
    print('YES')