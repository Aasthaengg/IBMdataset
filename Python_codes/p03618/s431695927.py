from collections import Counter

A = input()

N = len(A)
C = Counter(A)

print(1 + N * (N - 1) // 2 - sum(v * (v - 1) // 2 for v in C.values()))