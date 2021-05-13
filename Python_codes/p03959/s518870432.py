N = int(input())
T = [int(i) for i in input().split()]
A = [int(i) for i in input().split()] + [0]

MOD = 10**9 + 7

fixed = [False] * N
fixed[0] = True

for i in range(1, N):
    if T[i] > T[i-1]:
        fixed[i] = True

ans = 1
for i in range(N-1, -1, -1):
    if A[i] > A[i+1] and A[i] > T[i]:
        print(0)
        exit()
    if fixed[i] is True and A[i] < T[i]:
        print(0)
        exit()
    if fixed[i] is False and A[i] == A[i+1]:
        ans *= min(A[i], T[i])
        ans %= MOD
print(ans)
