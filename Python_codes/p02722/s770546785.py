N = int(input())
from math import sqrt

def divisor(num):
    max_num = int(sqrt(num))
    divisor_list = []
    for i in range(1, max_num + 1):
        if num % i == 0:
            divisor_list.append(i)
            divisor_list.append(num//i)
    return divisor_list

K0 = divisor(N)
K1 = divisor(N-1)
S = set(K1)
S.remove(1)
for k in K0:
    tmp = N
    if k == 1:
        continue
    while tmp % k == 0 and tmp >= k:
        tmp //= k
    if tmp % k == 1:
        S.add(k)
print(len(S))