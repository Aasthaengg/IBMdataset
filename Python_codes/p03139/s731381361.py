N, A, B = map(int, input().split())

M = None
m = None
if A + B <= N:
    M = min(A, B)
    m = 0
else:
    M = min(A, B)
    m = A + B - N

print(M, m)
