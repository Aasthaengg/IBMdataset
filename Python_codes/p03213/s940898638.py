import sys
n = int(input())
# 1とかの時例外処理

import math
def nCr(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def factorization(n):
    '''
    [base,power]のリストを返す
    '''
    arr = []
    temp = n
    for i in range(2, int(n**0.5) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i,cnt])
    if temp!=1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([n,1])

    return arr

base_power = [0] * 100
for i in range(2,n+1):
    arr = factorization(i)
    for base, power in arr:
        base_power[base] += power

More_2 = 0
More_4 = 0
More_14 = 0
More_24 = 0
More_74 = 0
for base in range(100):
    if base_power[base] >= 2:
        More_2 += 1
    if base_power[base] >= 4:
        More_4 += 1
    if base_power[base] >= 14:
        More_14 += 1
    if base_power[base] >= 24:
        More_24 += 1
    if base_power[base] >= 74:
        More_74 += 1

ans = 0
if More_2 - 2 > 0 and More_4 >= 2:
    ans += nCr(More_4,2)*(More_2-2)
if More_2 - 1 > 0 and More_24 > 0:
    ans += More_24 * (More_2-1)
if More_14 > 0 and More_4-1>0:
    ans += More_14 * (More_4-1)
if More_74 > 0:
    ans += More_74
print(ans)
