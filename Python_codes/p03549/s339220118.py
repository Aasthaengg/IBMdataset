N, M = map(int, input().split())
ms = 1900 * M + 100 * (N - M)
p = (1 / 2) ** M
print(int(ms*p**-1))
