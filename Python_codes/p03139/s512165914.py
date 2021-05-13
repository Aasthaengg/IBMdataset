N, A, B = map(int, input().split())
M = min(A, B)
if A + B <= N:
  m = 0
else:
  m = A + B - N
print(M, m)
