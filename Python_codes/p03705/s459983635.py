N, A, B = [int(_) for _ in input().split()]

print(max(0, B*(N-1) + A - (A*(N-1) + B) + 1))