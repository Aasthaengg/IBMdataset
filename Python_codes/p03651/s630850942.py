import fractions as f

N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
POSSIBLE = False

if K <= A[-1]:
    GCD = A[0]
    for i in range(1, N):
        GCD = f.gcd(GCD, A[i])
    if K % GCD == 0:
        POSSIBLE = True

if POSSIBLE:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")