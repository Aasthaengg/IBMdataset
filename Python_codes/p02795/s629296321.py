import numpy as np
import sys
h = int(input())
w = int(input())
n = int(input())
minhw = min(h,w)
maxhw = max(h,w)
cnt = 0
i = 0
while cnt<n:
    cnt += maxhw
    i += 1
print(i)