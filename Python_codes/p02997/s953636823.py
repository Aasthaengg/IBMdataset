N,K = map(int,input().split())
if N*(N-1)//2-(N-1) - K < 0:
    print(-1)
    exit()
M = N-1 + N*(N-1)//2-(N-1) - K
print(M)
for i in range(2,N+1):
    print(1,i)


r = N*(N-1)//2-(N-1) - K
for i in range(2,N+1):
    for j in range(i+1,N+1):
        if r == 0:
            exit()
        if r > 0:
            print(i,j)
            r -= 1