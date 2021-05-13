import fractions
N, K = map(int, input().split())
A = list(map(int, input().split()))
G = A[0]
for i in range(1,N):
  G = fractions.gcd(G,A[i])
if (K < max(A) and K % G == 0) or K == max(A):
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')
