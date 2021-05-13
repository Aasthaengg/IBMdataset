import fractions
N = int(input())
A = [int(input()) for _ in range(N)]
ans = A[0]
for i in range (1, N):
  ans = ans * A[i] // fractions.gcd(ans, A[i])
print(ans)