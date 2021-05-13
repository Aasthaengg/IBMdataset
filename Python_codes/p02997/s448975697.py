N,K = map(int,input().split())
M = (N-1)*(N-2)//2

if K > M:
    print(-1)
else:
    ans = N-1 + M - K
    print(ans)

    for i in range(1,N):
        print(i,N)
        ans -= 1

    for i in range(1,N):
        for j in range(i+1,N):
            if ans == 0:
                exit()
            else:
                print(i,j)
                ans -= 1