n, k = map(int, input().split())

A = list(map(int, input().split()))
import fractions
def list_gcd(X):
    t = max(X)
    for i in X:
        t = fractions.gcd(t, i)
    return t

if k in A or (k % list_gcd(A) == 0 and max(A) >= k):
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")