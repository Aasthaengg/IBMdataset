import fractions

n, k = map(int, input().split())
L = list(map(int, input().split()))
if n == 1:
    g = L[0]
else:
    g = fractions.gcd(L[0], L[1])
    for i in range(2, n):
        g = fractions.gcd(g, L[i])
M = max(L)
if M >= k and k % g == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
