N, K = map(int, input().split())
A = list(map(int, input().split()))
import fractions

if K > max(A):
    print('IMPOSSIBLE')
else:
    g = A[0]
    for i in range(N - 1):
        g = fractions.gcd(g, A[i + 1])
    #print(g)

    ok = False
    for val in A:
        if val >= K and (val - K) % g == 0:
            ok = True
    if ok:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')
