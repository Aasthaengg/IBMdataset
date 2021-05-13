from collections import defaultdict
from fractions import gcd
def lcm(x, y):
    return (x * y) // gcd(x, y)

N,M = map(int, input().split())
S = list(input())
T = list(input())

"""
存在するならば長さは必ずLである。
Lで存在しない場合、n * Lでも存在しない
"""
L = lcm(N, M)

X = defaultdict(str)

for p,s in enumerate(S):
    X[p * L // N] = s

flag = True
for q,t in enumerate(T):
    if X[q * L // M] and X[q * L // M] != t:
        flag = False
    else:
        X[q * L // M] = t

ans = L if flag else -1
print(ans)