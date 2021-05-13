from math import sqrt, floor
from collections import defaultdict
def comb(n,m):
    if m == 0:
        return 1
    return comb(n-1,m-1)*n // m
def facts(n):
    dic = defaultdict(int)
    for i in range(2,floor(sqrt(n))+1):
        while n % i == 0:
            n //= i
            dic[i] += 1
        if n == 1:
            break
    if n != 1:
        dic[n] += 1
    return dic
N, M = map(int,input().split())
mod = 10**9+7
ans = 1
dic = facts(M)
for p in dic:
    ans = (ans*(comb(dic[p]+N-1, dic[p]) % mod)) % mod
print(ans)
