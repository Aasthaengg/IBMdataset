N = int(input())
A = list(map(int, input().split()))

snk = A[0]
arg = sum(A)-snk
ans = abs(arg-snk)
for i in range(1, N-1):
  snk += A[i]
  arg -= A[i]
  dif = abs(arg-snk)
  ans = min(ans, dif)
print(ans)