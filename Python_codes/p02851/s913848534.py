N, K = map(int, input().split())
A = [0] + [int(a) - 1 for a in input().split()]
for i in range(1, N+1):
    A[i] = (A[i] + A[i-1]) % K

D = {0: 1}
ans = 0
for i in range(1, N+1):
    if i >= K:
        D[A[i-K]] -= 1
    a = A[i]
    if a not in D: D[a] = 0
    ans += D[a]
    D[a] += 1
print(ans)