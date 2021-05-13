N, A, B = map(int, input().split())
C = A + B - N
if C < 0:
    C = 0
print(min(A, B), C)
