N, M = map(int, input().split())

A = [None] * N
B = [None] * N

for i in range(N):
    a, b = map(int, input().split())
    A[i] = a
    B[i] = b

C = zip(A, B)
C = sorted(C)

ans = 0
for a, b in C:
    if b >= M:
        ans += a * M
        break
    else:
        ans += a * b
        M -= b

print(ans)
