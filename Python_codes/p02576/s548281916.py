N, X, T = [int(v) for v in input().split()]

n = p = 0

while n < N:
    p += T
    n += X

print(p)