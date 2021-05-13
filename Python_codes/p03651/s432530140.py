import fractions

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = []
for a1, a2 in zip(A, A[1:]):
    B.append(abs(a2-a1))

if K > max(A):
    print('IMPOSSIBLE')
    exit()
if K in A:
    print('POSSIBLE')
    exit()

g = B[0]
for b in B[1:]:
    g = fractions.gcd(g, b)

if (A[0] - K) % g == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')
