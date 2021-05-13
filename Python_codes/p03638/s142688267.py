from sys import stdin
from itertools import groupby
import numpy as np

h,w = [int(x) for x in stdin.readline().rstrip().split()]
n = int(stdin.readline().rstrip())
li = list(map(int,stdin.readline().rstrip().split()))

lin = np.asarray([0]*h*w)
now = 0
point = 0
for i in range(n):
    point += 1
    for j in range(now,li[i]+now):
        lin[j] = point
    now += li[i]

lin = np.reshape(lin,(h,w)).tolist()

for i in range(h):
    if i%2 == 1:
        lin[i] = lin[i][::-1]
    print(*lin[i])