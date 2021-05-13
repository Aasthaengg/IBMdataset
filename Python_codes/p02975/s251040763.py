# -*- coding: utf-8 -*-
N = int(input())
import collections
a_frq_dict = collections.Counter(map(int, input().split(' ')))

n = len(a_frq_dict)

if n == 1:
    if a_frq_dict[0]:
        print('Yes')
        exit()

elif n == 2:
    if N % 3 == 0 and a_frq_dict[0] == (N//3):
        print('Yes')
        exit()

elif n == 3:
    if N % 3 == 0:
        if all([f == (N//3) for f in a_frq_dict.values()]):
            values = list(a_frq_dict.keys())
            v = values[0] ^ values[1] ^ values[2]
            if v == 0:
                print('Yes')
                exit()

print('No')


