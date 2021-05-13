N, M, D = map(int, input().split())

k = 0
if D == 0:
    k = N
else:
    k = 2*(N - D)

print((M - 1)*k/N/N)