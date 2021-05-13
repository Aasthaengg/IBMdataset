N, X, T = map(int, input().split() )

a = (N + X - 1) // X
a = a * T

print(a)