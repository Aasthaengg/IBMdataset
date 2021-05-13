from math import gcd
n,k = map(int,input().split())
A = list(map(int,input().split()))
g = A[0]
m = max(A)
for x in A:
    g = gcd(g,x)
print("POSSIBLE" if k%g == 0 and m >= k else "IMPOSSIBLE")