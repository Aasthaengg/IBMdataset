import sys
import numpy as np
n, k, q = map(int, input().split())
a = [int(input())-1 for _ in range(q)]
lst = np.full(n, k)
for i in a:
    lst[:i]-=1
    lst[i+1:]-=1
for i in range(n):
    if lst[i] > 0:
        print('Yes')
    else:
        print('No')

