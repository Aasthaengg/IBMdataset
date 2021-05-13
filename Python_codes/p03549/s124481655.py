N, M = map(int, input().split())

A = (100 * (N - M) + 1900 * M) / pow(2, M)

B = 0
r = 1 / pow(2, M)
for i in range(1, 10 ** 5):
    B += i * pow(1 - r, i - 1)

print(int(round(A * B, 0)))
