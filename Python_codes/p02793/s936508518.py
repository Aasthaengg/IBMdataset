### 素因数分解する。
from collections import defaultdict

def factorize(n):
    """

    """
    tmp = n
    for i in range(2, int(n**0.5)+1):
        if tmp % i==0:
            cnt = 0
            while tmp % i == 0:
                cnt += 1
                tmp //= i
            if i in LCM:
                LCM[i] = max(LCM[i], cnt)
            else:
                LCM[i] = cnt
    if tmp != 1:
        if tmp in LCM:
            LCM[tmp] = max(LCM[tmp], 1)
        else:
            LCM[tmp] = 1
    if not LCM:
        if n in LCM:
            LCM[n] = max(LCM[n], 1)
        else:
            LCM[n] = 1
def inv(n, p):
    return pow(n, p-2, p)

LCM = dict()
N = int(input())
A = list(map(int, input().split()))
mod = 10**9+7

for i in range(N):
    if A[i] != 1:
        factorize(A[i])

lcm = 1
for key, val in LCM.items():
    lcm *= pow(key, val, mod)
    lcm %= mod

inv_sum = 0
for i in range(N):
    inv_sum += inv(A[i], mod)
    inv_sum %= mod

print(lcm * inv_sum % mod)