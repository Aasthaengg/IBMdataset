MOD = 10 ** 9 + 7

N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))

T_d = [1] * N
T_d[0] = T[0]
for i in range(1, N):
    if T[i - 1] < T[i]:
        T_d[i] = T[i]

A_d = [1] * N
A_d[-1] = A[-1]
for i in range(N - 2, -1, -1):
    if A[i] > A[i + 1]:
        A_d[i] = A[i]

# print (T)
# print (T_d)
# print ()
# print (A)
# print (A_d)

ans = 1
for i in range(N):
    tmp = max(0, min(A[i], T[i]) - max(A_d[i], T_d[i]) + 1)
    ans *= tmp
    ans %= MOD

print (ans)