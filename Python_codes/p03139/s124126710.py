N, A, B = map(int, input().split())
print(B if A > B else A, end=" ")
z = A + B - N
print(z if z > 0 else 0)