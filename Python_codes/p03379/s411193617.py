import numpy as np
import copy

N = int(input())
X = [int(i) for i in input().split()]

max_value = max(X)
min_value = min(X)

tmp_list = copy.deepcopy(X)
tmp_list.sort()
all_med = tmp_list[int((len(tmp_list)+1) / 2) - 1]

tmp_list.remove(max_value)
min_med = tmp_list[int((len(tmp_list)+1) / 2) - 1]

tmp_list = copy.deepcopy(X)
tmp_list.remove(min_value)
tmp_list.sort()
max_med = tmp_list[int((len(tmp_list)+1) / 2) - 1]

for i in range(N):
    if X[i] <= all_med:
        print(int(max_med))
    else:
        print(int(min_med))