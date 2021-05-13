import sys
input = sys.stdin.readline
N, K = [int(x) for x in input().strip().split()]
A = [int(x) for x in input().strip().split()]

if K > max(A):
    print('IMPOSSIBLE')
    exit()
if K in A:
    print('POSSIBLE')
    exit()

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

gcd_ = A[0]
for a in A[1:]:
    gcd_ = gcd(gcd_, a)

if K % gcd_ == 0:
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')