import itertools
from collections import Counter
from math import factorial

N = int(input())


def factorization(n):
    arr = dict()
    temp = n
    for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr[i] = cnt

    if temp != 1:
        arr[temp] = 1

    if not arr and n != 1:
        arr[n] = 1

    return arr


ans = 0
ct = Counter()
for i in range(2, N + 1):
    ct += Counter(factorization(i))


def solve(*exps):
    ret = 0
    for t in itertools.permutations(ct.values(), len(exps)):
        if all(t[i] - exps[i] >= 0 for i in range(len(exps))):
            ret += 1
    for x in Counter(exps).values():
        ret //= factorial(x)
    return ret


print(solve(2, 4, 4) + solve(14, 4) + solve(24, 2) + solve(74))
