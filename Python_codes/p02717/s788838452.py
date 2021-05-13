A, B, C = list(map(int, input().split()))

A, B = B, A
A, C = C, A
print(A, B, C)