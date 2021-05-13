A, B = map(int, input().split())
print(A + B if B / A == int(B / A) else B - A)
