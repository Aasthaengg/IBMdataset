n=int(input())
for i in range(n):
    a,b,c = input().split()
    x = int(a)
    y = int(b)
    z = int(c)
    p = [x,y,z]
    p.sort()
    if pow(p[0],2) + pow(p[1],2) == pow(p[2],2):
        print('YES')
    else:
        print('NO')
