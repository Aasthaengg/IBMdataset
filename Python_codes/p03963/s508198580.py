N, K = [int(_) for _ in input().split()]

cases = K

for n in range(N-1):
    cases *= (K - 1)

print(cases)