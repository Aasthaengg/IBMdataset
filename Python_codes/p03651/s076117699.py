from fractions import gcd
N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]
g = A[0]
for a in A[1:]:
    g = gcd(a, g)
for a in A:
    if a >= K and (a - K) % g == 0:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
