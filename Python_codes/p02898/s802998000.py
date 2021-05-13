import sys
input = sys.stdin.readline
from collections import defaultdict, deque
from bisect import bisect_left

(n, k), s = map(int, input().split()), sorted(list(map(int, input().split())))
print(len(s[bisect_left(s, k):]))