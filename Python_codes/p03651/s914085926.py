from fractions import gcd

N, K = map(int, input().split())
A = list(map(int,input().split()))

g = A[0]
for i in range(1, N):
  g = gcd(g, A[i])

if K > max(A):
  print("IMPOSSIBLE")
elif K % g != 0:
  print("IMPOSSIBLE")
else:
  print("POSSIBLE")