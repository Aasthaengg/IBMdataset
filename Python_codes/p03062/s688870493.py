import math
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import product
from collections import defaultdict
from collections import deque
from collections import Counter
import heapq


def input_li():
    return list(map(int, input().split()))


def input_int():
    return int(input())


N = input_int()
A_LI = input_li()
minus_cnt = 0
for a in A_LI:
    if a < 0:
        minus_cnt += 1

ans = 0
abs_min = 10 ** 9
for a in A_LI:
    ans += abs(a)
    abs_min = min(abs_min, abs(a))
print(ans) if minus_cnt % 2 == 0 else print(ans - abs_min * 2)
