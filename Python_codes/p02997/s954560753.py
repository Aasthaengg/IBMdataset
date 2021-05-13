n,k = map(int,input().split())
if k>(n-1)*(n-2)//2:
    print(-1)
else:
    print((n-1) + ((n-1)*(n-2)//2-k))
    for i in range(2, n+1):
        print(1, i)
    rem = (n-1)*(n-2)//2 - k
    cnt = 0
    for i in range(2, n+1):
        if cnt == rem:
            break
        for j in range(i+1, n+1):
            cnt += 1
            print(i, j)
            if cnt == rem:
                break