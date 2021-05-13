K = int(input())
N = 50

x, y = divmod(K, N)
base = 49 + x
rest = y
A = [None] * N
for i in range(N):
    A[i] = base - rest + (rest >= N - i) * (N + 1)

print(N)
print(*A)
