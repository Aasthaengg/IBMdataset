import math

N = int(input())
v1 = [int(i) for i in input().strip().split()]
v2 = [int(i) for i in input().strip().split()]

# Manhattan distance
m1 = 0
for i in range(N):
    m1 += abs(v1[i] - v2[i])

print(float(m1))

# Euclidean distance
m2 = 0
for i in range(N):
    m2 += (v1[i] - v2[i]) ** 2

m2 = math.sqrt(m2)

print(float(m2))

# ??
m3 = 0
for i in range(N):
    m3 += abs(v1[i] - v2[i]) ** 3

m3 = m3 ** (1 / 3)

print(float(m3))

# Chebyshev distance
m4 = 0
for i in range(N):
    m4 = max(abs(v1[i]-v2[i]), m4)

print(float(m4))
