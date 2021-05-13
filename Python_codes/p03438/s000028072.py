# -*- coding: utf-8 -*-
N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

import math
n1 = sum([max(0, a-b)  for a, b in zip(A, B)])
n2 = sum([max(0, int(math.floor((b-a)/2))) for a, b in zip(A, B)])

if n2 >= n1:
    print('Yes')
else:
    print('No')



