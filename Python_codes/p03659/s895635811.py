N = int(input())
A = list(map(int, input().split()))
P = A[0]
Q = sum(A[1:])
m = abs(P-Q)
for i in range(1, N-1):
  P += A[i]
  Q -= A[i]
  m = min(m, abs(P-Q))
print(m)