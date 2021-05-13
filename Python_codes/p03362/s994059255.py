list_ = []

import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True

n = int(55555 / 5)

for i in range(1,n):
    cand = 1 + 5 * i
    if is_prime(cand):
        list_.append(cand)

k = int(input())

st = str()

for i in range(k):
    if i == 0:
        st  =  str(list_[i])
    else:
        st = st + ' ' + str(list_[i])

print(st)