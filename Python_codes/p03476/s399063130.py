import math
from itertools import accumulate

def eratosthenes(n):
    is_prime = [True for _ in range(n)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [i for i in range(1, n+1) if is_prime[i-1]]
    return table

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