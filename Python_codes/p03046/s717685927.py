M,K = map(int,input().split())
if K>=2**M:
    print(-1)
else:
    if M==1:
        if K==1:
            print(-1)
        elif K==0:
            print("1 0 0 1")
    else:
        A = []
        for i in range(2**M-1,-1,-1):
            if i==K:continue
            A.append(i)
        A.append(K)
        for i in range(2**M):
            if i==K:continue
            A.append(i)
        A.append(K)
        print(*A)