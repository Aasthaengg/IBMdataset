from collections import defaultdict as dd
from collections import Counter
import math
N = int(input())
a = list(map(int, input().split()))
MOD = 10**9+7
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
    return Counter(fct)

fact_list = [dd(int) for _ in range(N)]
dic = dd(int)
for i,val in enumerate(a):
    tmp = factorize(val)
    for k,v in tmp.items():
        dic[k] = max(dic[k], v)

lcm = 1
for k,v in dic.items():
    lcm = (lcm*pow(k,v,MOD))%MOD
res = 0
for val in a:
    res = (res+pow(val, MOD-2, MOD))%MOD
res = (res*lcm)%MOD
print(res)
