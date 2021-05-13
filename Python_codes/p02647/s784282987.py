import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
A2 = [0]*(N+1)
for i in range(K):
    for j in range(N):
        g = math.ceil(j+1-A[j]-0.5)
        if g<1:
            g=1
        h = math.floor(j+1+A[j]+0.5)
        if h>N:
            h=N
        A2[g-1]+=1
        A2[h]-=1
    A[0]=A2[0]
    for j in range(1, N):
        A[j]=A[j-1]+A2[j]
    A2 = [0]*(N+1)
    c = 0
    for p in range(N):
        c+=A[p]
    if c >= N*N:
        break

print(*A)