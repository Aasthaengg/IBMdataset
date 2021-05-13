n=int(input())
for i in range(n):
    p=list(map(int,input().split(" ")))
    p.sort()
    a=p[0]
    b=p[1]
    c=p[2]
    if pow(a,2) + pow(b,2) == pow(c,2):
        print('YES')
    else:
        print('NO')
