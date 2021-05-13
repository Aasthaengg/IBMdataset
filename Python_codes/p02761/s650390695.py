# import itertools
# import math
# import sys
# import numpy as np

# N = int(input())
# S = input()
# n, *a = map(int, open(0))
N, M = map(int, input().split())
# A = list(map(int, input().split()))
# Q = list(map(int, input().split()))
# S = input()

# d = sorted(d.items(), key=lambda x:x[0]) # keyでsort

conditions = []
for i in range(M):
    conditions.append(list(map(int, input().split())))

ans = -1

for i in range(1000):
    i_str = str(i)
    if len(i_str) == N:
        # print(i)
        for condition in conditions:
            # print(condition)
            if i_str[condition[0] - 1] != str(condition[1]):
                # print("a")
                break
        else:
            ans = i
            break
    # print(i)


print(ans)