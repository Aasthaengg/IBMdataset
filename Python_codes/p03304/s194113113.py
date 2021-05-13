N, M, D = [int(_) for _ in input().split()]
print((1 + (D > 0)) * (N - D) * (M - 1) / N**2)
