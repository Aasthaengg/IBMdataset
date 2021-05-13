def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

N, K = map(int, input().split())
A = list(map(int, input().split()))
if max(A) < K:
    print('IMPOSSIBLE')
    exit()
res = A[0]
for i in range(1, N):
    a = A[i]
    b = res
    if a < b:
        a, b = b, a
    res = gcd(a, b)
if K % res == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')