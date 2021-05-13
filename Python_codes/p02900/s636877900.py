A, B = map(int, input().split())
from fractions import gcd
g = gcd(A,B)

#素因数分解して列挙する関数、約数列挙ではない！
def factorize(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    fct = list(set(fct))
    return fct

f = factorize(g)
ans = len(f)+1
print(ans)