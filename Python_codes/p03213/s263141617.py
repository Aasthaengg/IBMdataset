from itertools import product
from collections import defaultdict
n = int(input())


def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i == 0:
            cnt = 0
            while temp % i == 0:
                cnt += 1
                temp //= i
            arr.append([i, cnt])

    if temp != 1:
        arr.append([temp, 1])

    if arr == []:
        arr.append([n, 1])

    return arr


d = defaultdict(lambda: 0)
for i in range(2, n+1):
    a = factorization(i)
    for aa, k in a:
        d[aa] += k
t = [v for v in d.values()]


def num(t, a):
    return sum([1 if tt >= a-1 else 0 for tt in t])


print(num(t, 75) +
      num(t, 25)*(num(t, 3)-1) +
      num(t, 15)*(num(t, 5)-1) +
      num(t, 5)*(num(t, 5)-1)*(num(t, 3)-2)//2)
