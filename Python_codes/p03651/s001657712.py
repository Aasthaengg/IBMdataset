import fractions

n, k = map(int, input().split())
A = sorted(list(map(int, input().split())))

g = A[-1]
for a in A:
    g = fractions.gcd(a, g)

if k % g == 0 and k <= A[-1]:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
