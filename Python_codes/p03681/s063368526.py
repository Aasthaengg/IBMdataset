import math

N, M = map(int, input().split())
if abs(N - M) >= 2:
    print(0)
    exit()


N = math.factorial(N) % (10 ** 9 + 7)
M = math.factorial(M) % (10 ** 9 + 7)
if N == M:
    print((N * M * 2) % (10 ** 9 + 7))
else:
    print((N * M) % (10 ** 9 + 7))
