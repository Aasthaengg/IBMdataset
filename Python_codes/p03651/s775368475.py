from fractions import gcd

N, K = map(int, input().split())
As = list(map(int, input().split()))
if len(As) == 1:
    possible = (As[0] == K)
else:
    g = max(abs(As[1] - As[0]), 1)
    for A in As[2:]:
        g = gcd(g, A - As[0])

    possible = ((K-As[0]) % g == 0) and (min(As) <= K <= max(As))

if possible:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")