from fractions import gcd
n,k = map(int,input().split())
a = list(map(int,input().split()))
M = a[0]
g = a[0]
for i in range(1,n):
    M = max(M,a[i])
    g = gcd(g,a[i])
if k <= M and k % g == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")