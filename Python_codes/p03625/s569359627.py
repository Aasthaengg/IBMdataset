import collections
import sys
sys.setrecursionlimit(2000000)
# import math
# import itertools
# import statistics
# import numpy as np
n = int(input())
a = list(map(int, input().split()))
a_count = collections.Counter(a)
a_list = list(a_count.items())
a_sorted = sorted(a_list, key=lambda x: x[0], reverse=True)
# print(a_sorted)

ans = []
kouho = []
for i in range(len(a_sorted)):
    if a_sorted[i][1] >= 4:
        b = a_sorted[i][0]
        kouho.append(b)
        ans.append(b*b)
    if a_sorted[i][1] >= 2:
        kouho.append(a_sorted[i][0])


if len(ans) == 0 and len(kouho) < 2:
    print(0)
else:
    if len(ans) == 0:
        print(kouho[0]*kouho[1])
    else:
        print(max(max(ans), kouho[0]*kouho[1]))
