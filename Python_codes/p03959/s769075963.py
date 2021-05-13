N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
if T[0] > A[0] or T[-1] < A[-1]:
    print(0)
    exit()
for i in range(1, N):
    if T[i-1] != T[i] and T[i] > A[i]:
        print(0)
        exit()
    if A[N-i-1] != A[N-i] and A[N-i-1] > T[N-i-1]:
        print(0)
        exit()
h = [-1] * N
h[0] = T[0]
h[-1] = A[-1]
for i in range(1, N-1):
    if T[i] != T[i-1]:
        h[i] = T[i]
    if A[i] != A[i+1]:
        h[i] = A[i]
ans, mod = 1, 10**9+7
for i in range(1, N-1):
    if h[i] == -1:
        ans = ans * min(A[i], T[i]) % mod
print(ans) 