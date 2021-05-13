from fractions import gcd
def check():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    if K > max(A):
        return False
    g = A[0]
    for i in range(1,N):
        g = gcd(g,A[i])
    if K%g != 0:
        return False
    return True
if check():
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')