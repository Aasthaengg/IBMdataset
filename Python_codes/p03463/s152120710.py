n,a,b = map(int,input().split())
while True:
    if a + 1 == b:
        if a - 1 == 0:
            print('Borys')
            exit(0)
        else:
            a -= 1
    else:
        a += 1
    if b - 1 == a:
        if b + 1 == n + 1:
            print('Alice')
            exit(0)
        else:
            b += 1
    else:
        b -= 1    