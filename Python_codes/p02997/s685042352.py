n,k = map(int,input().split())

if k > (n-1) * (n-2) // 2:
    print(-1)
else:
    print((n-1) * n // 2 - k)
    count = 0
    for i in range(1,n+1):
        for j in range(i+1,n+1):
            print(i,j)
            count += 1
            if count == (n-1) * n // 2 - k:
                exit()
