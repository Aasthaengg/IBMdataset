A, B = map(int, input().split())
print(max(A, B) * 2 - 1 if abs(A - B) >= 2 else A + B)
