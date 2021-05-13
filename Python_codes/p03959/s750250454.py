N = int(input())
T = list(map(int,input().split()))
A = list(map(int,input().split()))
MOD = 10**9+7

ans = 1
for i in range(N):
    min_t = min_a = 1
    if i == 0 or T[i-1] < T[i]:
        min_t = T[i]
    if i == N-1 or A[i+1] < A[i]:
        min_a = A[i]
    if min_t > A[i] or min_a > T[i]:
            print(0)
            exit()
    n = min(T[i],A[i]) - max(min_t,min_a) + 1
    ans = (ans * n) % MOD
print(ans)