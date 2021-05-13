from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

def combination(n, k):
    numer = denom = 1
    for i in range(k):
        numer = numer * (n-i)
        denom = denom * (i+1)
    return numer // denom

N, A, B = map(int, input().split())
v = list(map(int, input().split()))
v.sort()
ave = sum(v[N-A:]) / A
x = v[N-A]
comb = 0
if x == v[-1]:
    n = N - bisect_left(v, x)
    for k in range(A, min(B, n)+1):
        comb += combination(n, k)
else:
    n = bisect_right(v, x) - bisect_left(v, x)
    k = bisect_right(v, x) - (N - A)
    comb = combination(n, k)
print(ave)
print(comb)