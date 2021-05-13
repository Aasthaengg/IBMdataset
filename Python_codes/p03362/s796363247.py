#ABC096-D Five, Five Everywhere
"""
問題：
55555以下の異なる素数をN個出力せよ。
但し、N個のうちどの5つの素数を組み合わせても素数にならないように
しなければならない。
このような数列は必ず作れるものと仮定して良い。(5<=N<=55)
解法：
5で割って1余る素数の個数は55555以下のうち1408個存在する。
よってこのうち適当にN個とって出力すれば良い。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n = int(readline())

import math
#nまでの素数のリスト
def eratosthenes(n): #必要な分だけ用意
    if n < 2: #1は素数ではない
        return []
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p: #limit=root(n)
            return prime + data #root(n)まで判定すれば、残りは全て素数であると言える
        prime.append(p)
        data = [e for e in data if e % p != 0] #エラトステネスのふるい

primes = eratosthenes(55555+1)

#debug
"""
res = 0
for i in primes:
    if i%5==1:
        res += 1
print(res) #1408
"""
ans = []
for i in primes:
    if n <= 0:
        break
    if i%5==1:
        ans.append(i)
        n -= 1

print(*ans)