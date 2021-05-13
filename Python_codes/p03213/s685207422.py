# 素因数分解によってx=p**n+q**m+...と表せるとき、
# 約数の個数は(n+1)*(m+1)*...
# つまり、約数が75個(素因数分解すると3*5*5)あるというのは素数が
# [2, 4, 4]個ずつor[4, 14]個ずつor[2, 24]個ずつor[74]個ある組み合わせを数えればよい

from collections import Counter, defaultdict
from itertools import product

n = int(input())

def prime_factorization(n):
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

prime = []
for i in range(1, n+1):
    prime += prime_factorization(i)
    
ctr = Counter(prime)

# 各素数が[2, 4, 14, 24, 74]個以上ある素数を求める
d = defaultdict(list)
for k, v in ctr.items():
    for p in [2, 4, 14, 24, 74]:
        if v >= p:
            d[p].append(k)
        else:
            break

            
# 組み合わせ(重複している組みあわせはcontiue)
comb_num = 0
for comb in [[2, 4, 4], [4, 14], [2, 24], [74]]:
    for prime_comb in list(product(*[d[c] for c in comb])):
        if len(prime_comb) != len(set(prime_comb)):
            continue
        if comb == [2, 4, 4] and prime_comb[1] < prime_comb[2]:
            continue
        comb_num += 1
print(comb_num)            