import sys, bisect, math

N, K = map(int, input().split())
A = list(map(int, sys.stdin.readline().rsplit()))

A.sort()
if bisect.bisect_left(A, K) == N:
    print("IMPOSSIBLE")
    exit()

a = A[0]
for aa in A[1:]:
    a = math.gcd(a, aa)

if K % a != 0:
    print("IMPOSSIBLE")
else:
    print("POSSIBLE")
