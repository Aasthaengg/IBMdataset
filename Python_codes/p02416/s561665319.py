while True:
    a=list(input())
    if a[0]=='0':
        break
    g=0
    for i in a:
        g+=int(i)
    print(g)
