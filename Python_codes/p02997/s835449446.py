N,K = map(int,input().split())
M = (N-1)*(N-2)//2

if M >= K:
    print(M-K+N-1)
    for i in range(1,N):
        print(1,1+i)
    tmp = 0
    for i in range(2,N):
        for j in range(i+1,N+1):
            if tmp == M-K:
                break
            print(i,j)
            tmp += 1
else:
    print(-1)