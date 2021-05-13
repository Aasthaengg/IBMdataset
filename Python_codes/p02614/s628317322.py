# coding: utf-8
# Your code here!
import copy
import itertools
import numpy as np

h, w, k = map(int, input().split())

for i in range(h):
    row = list(input())
    # print(row)
    row = [0 if x=="." else 1 for x in row]
    row = np.array(row).reshape(1, w)
    if i == 0:
        c_matrix = row
    else:
        c_matrix = np.append(c_matrix, row, axis=0)
    
# print(c_matrix, "\n")
row_list = list(range(h))
col_list = list(range(w))
count = 0
for i in range(h+1):
    row_idx = list(itertools.combinations(row_list, i))
    for j in range(w+1):
        col_idx = list(itertools.combinations(col_list, j))
        # print(row_idx, col_idx)
        for row in row_idx:
            for col in col_idx:
                tmp = copy.deepcopy(c_matrix)
                tmp[row, :] = 0 
                tmp[:, col] = 0
                ans = np.sum(np.sum(tmp, axis=1))
                if ans == k:
                    count += 1
                    # print(tmp)
            
print(count)

