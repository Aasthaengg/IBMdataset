"""
---アルゴリズム概要---
Mを構成する素因数を、a1~aNの各スロットにいくつ置くのか、を考える問題。
まずは試し割りによってMを素因数分解。
重複組合せの公式で各素因数の配置パターンを算出し累乗していく。

試し割りは、O(√M)の計算量で処理できる。
√Mを超える素因数は、多くても一つしか存在しないため、√Mを超える値で試し割りをする必要はない。
もし√Mまでの値で試し割りを終えた段階で、Mを素因数分解しきれていなければ、残った商こそが√Mを超える唯一の素因数である。

簡単に証明
もし√Mを超える素因数が２つ存在しているとしよう。
それらは、(√M + α)と(√M + β)というふうに表すことができる。
この２つの積は明らかにMの値を超えてしまう。つまり前提に矛盾する。
したがって、√Mを超える素因数は多くても一つ
"""
from collections import Counter
import math

N,M = map(int,input().split())
factors = []

while M%2 == 0:
    M//=2
    factors.append(2)
    
f = 3
while f**2 <= M:
    while M%f==0:
        M//=f
        factors.append(f)
    f+=2
if M!=1:
    factors.append(M)

factors = Counter(factors)

ans = 1
for k in factors.values():
    ans *= math.factorial(k+N-1)//(math.factorial(N-1)*math.factorial(k))

print(ans%(10**9+7))