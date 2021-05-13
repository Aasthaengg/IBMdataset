from math import gcd
import numpy
N, M = map(int, input().split())
S = input()
T = input()
def func(m, n):
    return (m * n) // gcd(m, n)
ans = func(N, M)
var1 = ans//N
var2 = ans//M
for i in range(1, ans+1, var1*var2):
    varS = (i - 1) // var1
    varT = (i - 1) // var2
    if S[varS] != T[varT]:
        ans=-1
print(ans)