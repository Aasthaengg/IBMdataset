N = int(input())
P = [int(input()) for _ in range(N)]

L = [1]*(N+1)
for i in range(N):
    if P[i] < N and L[P[i]+1] == 1:
        L[P[i]+1] = L[P[i]]+1
    if L[P[i]] == 1:
        L[P[i]] = 0

ans = N-max(L)
print(ans)