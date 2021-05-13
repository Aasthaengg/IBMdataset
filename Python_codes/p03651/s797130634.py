import fractions
N, K = map(int, input().split())
A = list(map(int, input().split()))

g = A[0]
for a in A[1:]:
    g = fractions.gcd(g, a)

print("POSSIBLE" if K <= max(A) and K % g == 0 else "IMPOSSIBLE")