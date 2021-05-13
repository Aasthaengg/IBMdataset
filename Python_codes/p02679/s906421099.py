import math
import copy
from collections import defaultdict

def preproc(a,b): # a != 0 or b != 0
    if a < 0:
        a,b = -a,-b
    if a == 0 or b == 0:
        return (a, b)
    GCD = math.gcd(a,b)
    return (a // GCD, b // GCD)

n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
mod = 1000000007
dic = defaultdict(int)
A = 0
B = 0
AB = 0
for k,(a,b) in enumerate(ab):
    if a == 0 and b == 0:
        AB += 1
        n -= 1
        continue
    a,b = preproc(a,b)
    if a == 0:
        A += 1
        n -= 1
    elif b == 0:
        B += 1
        n -= 1
    else:
        dic[(a,b)] += 1
ok = (pow(2,A,mod) + pow(2,B,mod) - 1) % mod
c = copy.copy(dic)
for k,v in c.items():
    if not dic[k]:
        continue
    a,b = k
    pair = (b,-a) if b > 0 else (-b,a)
    if dic[pair]:
        ok *= pow(2,v,mod) + pow(2,dic[pair],mod) - 1
        ok %= mod
        n -= v + dic[pair]
        dic[pair] = 0
ans = ok * pow(2,n,mod) - 1 + AB
ans %= mod
print(ans)