N = int(input())
K = int(input())
MIN = 10 ** 8
for i in range(N+1):
    MIN = min(MIN, 2 ** i + (N - i) * K)
print(MIN)