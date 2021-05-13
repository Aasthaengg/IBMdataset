import sys
import numpy as np
import math
import collections
import copy
from collections import deque 
from functools import reduce
from itertools import product
from itertools import combinations

# input = sys.stdin.readline

def get_prime_list(number):
    is_prime = np.ones(number, dtype=bool)
    is_prime[:2] = False
    num_sqrt = np.sqrt(number) + 1
    for i in range(2, int(num_sqrt) + 1):
        if (is_prime[i]):
            is_prime[i*2::i] = False
    prime_list = np.arange(number)[is_prime]
    return prime_list

Q = int(input())
LRn = [list(map(int, input().split())) for _ in range(Q)]
prime_list = get_prime_list(10**5)
prime_cnt = [0 for _ in range(10**5 + 10)]
for i in range(3, 10**5):
    if i in prime_list:
        if ((i+1)/2) in prime_list:
#             print(i)
            prime_cnt[i] = prime_cnt[i-1] + 1
            continue
    prime_cnt[i] = prime_cnt[i-1]
for LR in LRn:
    print(prime_cnt[LR[1]]-prime_cnt[LR[0]-1])











