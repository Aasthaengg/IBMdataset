_,a,b = map(int,input().split())
while 1:
    if a+1 != b:
        a += 1
    else:
        print('Borys')
        exit()
    if b-1 != a:
        b -= 1
    else:
        print('Alice')
        exit()