n = int(input())
a = [int(input()) for i in range(n)]

if 2 in a:
    k = 1
    while True:
        t = a[k-1]
        a[k-1] = -1
        k = t
#        print(t)
#        print(a)
        if k == -1:
            break
        elif k == 2:
            break
        
    if k == -1:
        print(-1)
    else:
        print(a.count(-1))
else:
    print(-1)