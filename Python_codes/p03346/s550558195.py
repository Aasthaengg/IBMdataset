N = int(input())
P = [int(input()) for _ in range(N)]
hist = [0 for _ in range(N+1)]
A = {i:0 for i in range(1,N+1)}
for i in range(N):
    a = P[i]
    if hist[a-1]==0:
        A[a] = a
    else:
        A[a] = A[a-1]
    hist[a] = 1
cmax = 0
for i in range(1,N+1):
    cmax = max(cmax,i-A[i]+1)
print(N-cmax)