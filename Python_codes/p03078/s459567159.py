import sys
import itertools
# import numpy as np
import time
import math

sys.setrecursionlimit(10 ** 7)

from collections import defaultdict

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

x, y, z, t = map(int, readline().split())
a = sorted(map(int, readline().split()), reverse=True)
b = sorted(map(int, readline().split()), reverse=True)
c = sorted(map(int, readline().split()), reverse=True)

ans = []

for i in range(len(a)):
    for j in range(len(b)):
        ans.append(a[i] + b[j])

ans = sorted(ans, reverse=True)
fin_ans = []
for j in range(len(c)):
    for i in range(min(len(ans), t)):
        fin_ans.append(ans[i] + c[j])

fin_ans = sorted(fin_ans, reverse=True)

for i in fin_ans[:t]:
    print(i)