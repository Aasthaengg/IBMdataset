import math
from itertools import accumulate

def eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = [2]
    limit = int(n**0.5)
    data = [i + 1 for i in range(2, n, 2)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

max_lr = 100000
er_list = eratosthenes(max_lr)
count = [0] * max_lr


for i in range(len(er_list)):
    if (er_list[i]+1)//2 in er_list:
        count[er_list[i]] = 1
            
count = list(accumulate(count))
            
Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())
    print(count[r]-count[l-1])