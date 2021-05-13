K = int(input())
N = 50
r = K % N
a = [N - 1 + K // N - r] * N
for i in range(r):
    a[i] += N + 1
print(N)
print(" ".join(map(str, a)))
