# -*- coding: utf-8 -*-
N = int(input())
S = input()

import collections
n_frq_dict = collections.defaultdict(int)
for s in S:
    n_frq_dict[s] += 1

mod=10**9+7
ret = 1
for frq in n_frq_dict.values():
    ret *= frq + 1
    ret %= mod
    
print(ret - 1)








