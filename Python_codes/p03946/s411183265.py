N, T = map(int,input().split())
A = list(map(int,input().split()))
m = [0]*N
M = [0]*N
m[0] = A[0]
for k in range(1,N):
    m[k] = min(A[k],m[k-1])

M[-1] = A[-1]
for k in range(N-2,-1,-1):
    M[k] = max(A[k],M[k+1])

D = [M[k]-m[k] for k in range(N)]
P = max(D)

ans = 0
for k in range(N):
    if A[k]-m[k] == P:
        ans += 1
print(ans)
