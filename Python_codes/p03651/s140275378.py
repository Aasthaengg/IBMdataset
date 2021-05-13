def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


N, K = map(int, input().split())
A = list(map(int, input().split()))
if K in A:
    print("POSSIBLE")
    exit()

max_val = max(A)
if max_val < K:
    print("IMPOSSIBLE")
    exit()

gcd_val = A[0]
for a in A[1:]:
    gcd_val = gcd(gcd_val, a)

ans = max_val
while K <= ans:
    if K == ans:
        print("POSSIBLE")
        exit()
    else:
        ans -= gcd_val
print("IMPOSSIBLE")