n, m = input().split()
n, m = int(n), int(m)
C = [int(c) for c in input().split()]

# Coin Changing Problem
T = [0] + [float('inf')] * n

for c in C:
    for j in range(c, n+1):
        T[j] = min(T[j], T[j - c] + 1)

print(T[-1])