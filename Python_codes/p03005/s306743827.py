import sys

# from collections import Counter, deque, defaultdict
# from itertools import accumulate, permutations, combinations, takewhile, compress, cycle
# from functools import reduce
# from math import ceil, floor, log10, log2, factorial

sys.setrecursionlimit(1000000)
MOD = 10 ** 9 + 7

N, K = [int(x) for x in input().split()]

print(N - K if K != 1 else 0)
