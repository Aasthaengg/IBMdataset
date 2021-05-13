from fractions import gcd
N, K = map(int, input().split())
A = list(map(int, input().split()))
if max(A) < K:
    print("IMPOSSIBLE")
else:
    temp = A[0]
    for a in A[1:]:
        temp = gcd(a, temp)
    if K % temp == 0:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")