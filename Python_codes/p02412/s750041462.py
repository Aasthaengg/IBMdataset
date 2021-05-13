while 1:
    list = [input().split()]
    n = int(list[0][0])
    x = int(list[0][1])
    i = 1
    j = 2
    k = 3
    cnt = 0
    if n == 0 and x == 0:
        break
    while 1 :
        for i in range(i,n-1):
            for j in range(i+1,n):
                for k in range(j+1,n+1):
                    if x == i + j + k:
                        cnt += 1
                k += 1
            j += 1
        i += 1
        if n-1 <= i:
            print(cnt)
            break