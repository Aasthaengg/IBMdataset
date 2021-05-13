N, M, X = map(int, input().split())
A = list(map(int, input().split()))

P = [0] * (N + 1)

for A in A:
    P[A] = 1

a = P[:X].count(1)
b = P[X - N:].count(1)

# print(P[:X])
# print(P[X - N:])
print(min(a, b))
