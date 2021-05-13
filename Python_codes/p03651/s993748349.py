from functools import reduce
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
def gcdlist(A):
    if len(A) == 1:
        return A[0]
    else:
        return reduce(gcd,A)

N,K = map(int,input().split())
A = list(map(int,input().split()))
ans = gcdlist(A)
if (K in A or (K%ans == 0)) and K <= max(A):
    print('POSSIBLE')
else:
    print('IMPOSSIBLE')