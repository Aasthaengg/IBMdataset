from math import gcd
import sys

N = int(input())

a = list(map(int,input().split()))

A = max(a)+1

# 全ての数に対して、入っているかいないかを判別する配列を作る
c = [0]*A
for i in range(N):
    c[a[i]] += 1

# print(c)

pairwise = True

for i in range(2,A):
    cnt = 0

    # 素因数ずつ数を増やしていき、同じ素因数を持つことがあればpairwiseではない
    # たとえば、3ならば、3,6,9,,と増やしていき、それがc[]に１つ以上含まれているか調べていく
    for j in range(i,A,i):
        cnt += c[j]
    if (cnt > 1):
        pairwise = False

if pairwise:
    print("pairwise coprime")
    sys.exit()

g = 0
for i in range(N):
    g = gcd(g,a[i])
if (g == 1):
    print("setwise coprime")
    sys.exit()

else:
    print('not coprime')