from fractions import gcd

N, K = map(int, input().split())
A = list(map(int, input().split()))
g = A[0]
for a in A:
  g = gcd(g, a)

B = [a - K for a in A if a >= K]
for b in B:
  if b % g == 0:
    print('POSSIBLE')
    quit()

print('IMPOSSIBLE')