from math import gcd
N, K = map(int, input().split())
A = list(map(int, input().split()))

if K > max(A):
    print("IMPOSSIBLE")
    exit()

x = A[0]

for i in range(1, N):
    x = gcd(A[i], x)

if K%x == 0:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")