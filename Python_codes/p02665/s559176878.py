N = int(input())
A = [int(a) for a in input().split()]

ans = 1
L = [0]*(N+2)
for i in range(N+1):
    L[i+1] = L[i]+A[i]

v = 1
for i in range(1, N+1):
    v = min(2*v, L[-1]-L[i])
    ans += v
    v -= A[i]
    if v < 0:
        ans = -1
        break
if A[0] > 0:
    ans = -1
    if N == 0 and A[0] == 1:
        ans = 1

print(ans)