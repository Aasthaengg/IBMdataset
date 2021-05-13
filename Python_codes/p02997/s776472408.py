N,K = map(int,input().split())
if K>((N-1)*(N-2))//2:
    print(-1)
else:
    print((N*(N-1))//2-K)
    for i in range(1,N):
        print(i,N)
    cnt = 0
    for i in range(1,N-1):
        for j in range(i+1,N):
            if cnt>=K:
                print(i,j)
            else:
                cnt += 1