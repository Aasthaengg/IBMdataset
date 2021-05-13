A, B, C = [int(_) for _ in input().split()]

x = min(A, C)
y = min(B + 1, C - x)

print(B + x + y)
