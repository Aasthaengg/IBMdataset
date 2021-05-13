N, L = map(int, input().split())
A = [L+i for i in range(N)]
total = 0
min_abs = 301

for i in range(N):
    total += A[i]
    if min_abs > abs(A[i]):
        min_abs = abs(A[i])
        idx = i

print(total - A[idx])
