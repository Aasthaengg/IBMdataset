from fractions import gcd

N,K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()

def gcd_all():
    x = A[0]
    for i in range(1, N):
        x = gcd(x, A[i])
    return x

def solve():
    if K > A[-1]:
        return False
    return K % gcd_all() == 0

print('POSSIBLE' if solve() else 'IMPOSSIBLE')