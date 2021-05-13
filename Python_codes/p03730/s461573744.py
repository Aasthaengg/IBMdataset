# Begin Header {{{
from math import gcd
from collections import Counter, deque, defaultdict
from heapq import heappush, heappop, heappushpop, heapify, heapreplace, merge
from bisect import bisect_left, bisect_right, bisect, insort_left, insort_right, insort
from itertools import accumulate, product, permutations, combinations, combinations_with_replacement
# }}} End Header
# _________コーディングはここから！！___________
# ... 最小側の制約も確認した？
# ... オーバーフローしない？
a, b, c = map(int, input().split())
for i in range(1, b+1):
    if (a*i-c)%b: i+=1
    else:
        print("YES")
        exit()
print("NO")