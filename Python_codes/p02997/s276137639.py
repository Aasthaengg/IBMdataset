N,K = map(int,input().split())
if (N-1)*(N-2)//2 < K:
    print(-1)
    exit()
M = (N-1) + ((N-1)*(N-2)//2-K)
c = 0
print(M)
#Start from tree with depth = 1
for i in range(2,N+1):
    print(1,i)
    c += 1
    if c >= M:
        exit()
for i in range(2,N):
    for j in range(i+1,N+1):
        print(i,j)
        c += 1
        if c >= M:
            exit()


