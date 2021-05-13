n,k = map(int,input().split())
if n*(n-1)//2 - (n-1) < k:
    print(-1)
else:
    e = n*(n-1)//2 - k
    print(e)
    cnt = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            print(i,j)
            cnt += 1
            if cnt == e:
                exit()
