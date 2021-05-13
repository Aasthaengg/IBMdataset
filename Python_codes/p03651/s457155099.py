import fractions

N,K = map(int,input().split())
A = list(map(int,input().split()))

n = A[0]
for i in range(N):
    n = fractions.gcd(n, A[i])

if K<=max(A) and K%n==0:
  print("POSSIBLE")
else:
  print("IMPOSSIBLE")