from math import gcd
from functools import reduce
from sys import exit

# O(NlogA+AloglogA)解
MAX_A = 1000000
lowerst_prime = [0] * (MAX_A + 1) # 最小の素因数をいれる(2以上をみていけばいい)
count = [0] * (MAX_A + 1) # 約数として出てくる回数を数える

for i in range(2, MAX_A + 1): # エラトステネスの篩
    if lowerst_prime[i] != 0:
        continue
    lowerst_prime[i] = i
    for j in range(i * i, MAX_A + 1, i): # i * iスタートでいいのは、i * bはbの約数でもあるため
        if lowerst_prime[j] == 0:
            lowerst_prime[j] = i
# 入力
N = int(input())
A = [*map(int, input().split())]

if reduce(gcd, A) != 1:
    print("not coprime")
    exit(0)

for i in range(N):
    while A[i] > 1:
        divide = lowerst_prime[A[i]]
        count[divide] += 1
        while A[i] % divide == 0: # 割れるだけ割る
            A[i] //= divide

for i in range(MAX_A + 1):
    if count[i] >= 2:
        print("setwise coprime")
        exit(0)
print("pairwise coprime")