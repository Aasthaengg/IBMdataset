N,M = map(int,input().split())
A = list(map(int,input().split()))
B = [0 for _ in range(N+1)]
for i in range(N):
    B[i+1] = (B[i]+A[i])%M
C = {}
for i in range(N+1):
    b = B[i]
    if b not in C:
        C[b] = 0
    C[b] += 1
cnt = 0
for b in C:
    k = C[b]
    cnt += (k*(k-1))//2
print(cnt)