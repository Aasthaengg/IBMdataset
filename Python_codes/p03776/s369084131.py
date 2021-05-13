import math
import copy
from operator import mul
from functools import reduce
from collections import defaultdict
from collections import Counter
from collections import deque
# 直積 A={a, b, c}, B={d, e}:のとき，A×B={(a,d),(a,e),(b,d),(b,e),(c,d),(c,e)}: product(A, B)
from itertools import product
# 階乗 P!: permutations(seq), 順列 {}_len(seq) P_n: permutations(seq, n)
from itertools import permutations
# 組み合わせ {}_len(seq) C_n: combinations(seq, n)
from itertools import combinations
from bisect import bisect_left, bisect_right

# import numpy as np
# from scipy.special import perm
# from scipy.special import comb

def inside(y, x, H, W):
    return 0 <= y < H and 0 <= x < W
 
# 四方向: 右, 下, 左, 上
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
 
def i_inpl(): return int(input())
def l_inpl(): return list(map(int, input().split()))
INF = float("inf")

########

def C(n,r):
    f = math.factorial
    return int(f(n) // f(r) // f(n-r))

N, A, B = l_inpl()
v = l_inpl()

sort_v = sorted(v, reverse=True)
ans_1 = sum(sort_v[:A])/A
print(ans_1)

max_v = sort_v[A-1]
max_v_count = sort_v.count(max_v)
max_v_count_in_ans = sort_v[:A].count(max_v)

if max_v != sort_v[0]: # 1つでも増やすと平均が減少する場合
    ans = C(max_v_count, max_v_count_in_ans)
else:
    ans = 0
    for i in range(A, min(B, max_v_count) + 1):
        ans += C(max_v_count, i)

print(int(ans))
