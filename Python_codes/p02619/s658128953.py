import sys
import numpy as np
from operator import mul
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

d = int(readline())
c = list(map(int, readline().split()))
s = []
for _ in range(d):
    add = list(map(int, readline().split()))
    s.append(add)

#t = [0] * d
day = 0
satisfy = 0
sumC = sum(c)
count = np.zeros(26)

for i in range(d):
    t = int(readline()) - 1
    up = s[day][t]
    count += 1
    count[t] = 0
    sub = map(mul, count, c)
    satisfy += (up - sum(sub))
    # satisfy
    print(int(satisfy))
    day += 1
