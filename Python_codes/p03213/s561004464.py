# coding: utf-8
import sys
from collections import defaultdict
import itertools

sr = lambda: sys.stdin.readline().rstrip()
ir = lambda: int(sr())
lr = lambda: list(map(int, sr().split()))

def prime_factorize(n): # Nの素因数分解
    a = []
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

# 約数の組み合わせ（３・５・５）（７５）など
N = ir()
dic = defaultdict(int)
for x in range(2, N+1):
    primes = prime_factorize(x)
    for p in primes:
        if p in dic:
            dic[p] += 1
        else:
            dic[p] = 1

answer = 0
for x, y, z in itertools.permutations(dic.values(), 3):
    if x >= 2 and y >= 4 and z >= 4:
        answer += 1

answer //= 2
for x, y in itertools.permutations(dic.values(), 2):
    if x >= 4 and y >= 14:
        answer += 1
    if x >= 2 and y >= 24:
        answer += 1

for x in dic.values():
    if x >= 74:
        answer += 1

print(answer)
# 40