N,K = map(int,input().split())
if N==2:
    if K==0:
        print(1)
        print(1,2)
    elif K==1:
        print(-1)
elif N==3:
    if K==0:
        print(3)
        print(1,2)
        print(2,3)
        print(1,3)
    elif K==1:
        print(2)
        print(1,2)
        print(1,3)
    elif K>=2:
        print(-1)
elif N==4:
    if K==0:
        print(6)
        print(1,2)
        print(1,3)
        print(1,4)
        print(2,3)
        print(2,4)
        print(3,4)
    elif K==1:
        print(5)
        print(1,3)
        print(1,4)
        print(2,3)
        print(2,4)
        print(3,4)
    elif K==2:
        print(4)
        print(1,3)
        print(1,4)
        print(2,4)
        print(3,4)
    elif K>=3:
        print(-1)
else:
    if K>((N-1)*(N-2))//2:
        print(-1)
    else:
        A = [(i,j) for i in range(1,N) for j in range(i+1,N+1)]
        i = 2
        j = 3
        cnt = 0
        while cnt<K:
            if (i,j) in A:
                A.remove((i,j))
            j += 1
            if j>N:
                i += 1
                j = i+1
            cnt += 1
        print((N*(N-1))//2-K)
        for a in A:
            print(a[0],a[1])