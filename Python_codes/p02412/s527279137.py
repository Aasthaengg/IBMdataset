while(True):
    n,x = [int(i) for i in input().split()]
    if(n == 0 and x == 0):
        break
    t = 0
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            for k in range(1,n + 1):
                if(i < j < k and i + j + k == x):
                    t += 1
    print(t)