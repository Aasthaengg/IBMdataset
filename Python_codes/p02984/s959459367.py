N = int(input())
A = list(map(int, input().split()))

x2 = 0

for i in range(N):
    if i % 2 == 0:
        x2 += A[i]
    else:
        x2 -= A[i]

R = [0] * N
R[0] = x2

for i in range(N - 1):
    R[i + 1] = 2 * A[i] - R[i]
print(*R)
