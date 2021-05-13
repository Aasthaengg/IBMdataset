"""
---アルゴリズム概要---
Mを素因数分解する。
各素因数をa1 ~ an をどの場所にいくつ納めるかを考えれば、それが答えになる。
"""
import math
from collections import Counter
N,M = map(int,input().split())
a = []
def prime_factorize(n):
        while n % 2 == 0:
            a.append(2)
            n //= 2
        f = 3
        while f * f <= n:
            if n % f == 0:
                a.append(f)
                n //= f
            else:
                f += 2
        if n != 1:
            a.append(n)
        return a

prime_factorize(M)
#次に各要素の配置パターン数を求めて累積していく。
#combination関数を定義する
def combination(n,r):
    return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

factors = Counter(a)
ans = 1
for k,v in factors.items():
    ans *= combination(N+v-1,v)

print(ans%(10**9+7))