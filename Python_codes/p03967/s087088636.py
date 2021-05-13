import sys
#import numpy as np

stdin = sys.stdin

ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split())) # applies to numbers only
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

S = list(rs())
p_cnt = S.count('p')
g_cnt = len(S) - p_cnt
possible = (g_cnt-p_cnt) // 2
print(possible)
# 44