"""
---アルゴリズム概要---
a1 ~ anの各スロットに、Mの各素因数をいくつ置くか、という問題。
まずは、Mを素因数分解し、それから重複組み合わせの容量で、各素因数ごとに配分パターンを算出。
それらの配分パターンを素因数間でかけ合わせると、答えとなる。

Mの素因数分解は、試し割り法という最もシンプルな方法で行う。
"""
from collections import Counter
import math
N,M = map(int,input().split())
factors = []
while True:
    if M % 2 == 0:
        M //= 2
        factors.append(2)
    else:
        break
f = 3
while f**2 <= M:
    if M % f == 0:
        M //= f
        factors.append(f)
    else:
        f += 2
if M != 1:
    factors.append(M)

counter = Counter(factors)
ans = 1
for r in counter.values():
    ans *= math.factorial(N+r-1)//(math.factorial(N-1)*math.factorial(r))

print(ans%(10**9+7))