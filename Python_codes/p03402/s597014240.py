# import numpy as np
import sys, math, heapq
from itertools import permutations, combinations
from collections import defaultdict, Counter, deque
from math import factorial, gcd
from bisect import bisect_left, bisect_right

sys.setrecursionlimit(10 ** 7)
MOD = 10 ** 9 + 7
input = lambda: sys.stdin.readline()[:-1]
pl = lambda x: print(*x, sep="\n")
# conv_matrix = lambda l: ["".join(l[i : i + 100]) for i in range(0, len(l), 100)]
A, B = map(int, input().split())

mat = [["."] * 100 for _ in range(50)] + [["#"] * 100 for _ in range(50)]
# for mati in mat:
#     print("".join(mati))

# mat[0][3] = "#"
# mat[3][6] = "#"
# for mati in mat:
#     print("".join(mati))
# exit()

black_count = 1
white_count = 1

for i in range(0, 50, 2):
    if black_count == B:
        break
    for j in range(0, 100, 2):
        if black_count == B:
            break
        mat[i][j] = "#"
        black_count += 1
for i in range(1, 50, 2):
    if white_count == A:
        break
    for j in range(0, 100, 2):
        if white_count == A:
            break
        mat[-i][j] = "."
        white_count += 1

print(100, 100)
for mati in mat:
    print("".join(mati))
