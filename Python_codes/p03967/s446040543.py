import sys
import math
import fractions
from collections import deque
from collections import defaultdict
sys.setrecursionlimit(10**7)

s = input()
size = len(s)
p_cnt = s.count("p")

max_p = size // 2

print(max_p - p_cnt)
