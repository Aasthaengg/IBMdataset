import sys
import numpy as np
from collections import Counter
from math import factorial

stdin = sys.stdin
 
ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N, M = rl()
A = np.array(rl())
A_cum = A.cumsum()
A_cum %= M
A_cum = A_cum.tolist()
c = Counter(A_cum)
answer = 0

for k, v in c.items():
    if k == 0:
        answer += v
    if v >= 2:
        answer += factorial(v) // factorial(2) // factorial(v-2)

print(answer)
#13
