import math
from collections import defaultdict, Counter

def prime_factorize(n):
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

N = int(input())
A = [int(i) for i in input().split()]
v_list = []
mod = 10 ** 9 + 7
LCM_dict = defaultdict(int)
for i in range(N):
    prime_cnt = Counter(prime_factorize(A[i]))
    for k, v in prime_cnt.items():
        LCM_dict[k] = max(LCM_dict[k], v)
    v_list.append(prime_cnt)
ans = 0
for i in range(N):
    prime_cnt = v_list[i]
    tmp_value = 1
    for k, v in LCM_dict.items():
        cnt = 0 if k not in prime_cnt.keys() else prime_cnt[k]
        tmp_value = pow(k, v - cnt) * tmp_value
        tmp_value = tmp_value % mod
    ans += tmp_value
    ans = ans % mod
print(ans)