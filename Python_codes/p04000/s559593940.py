import numpy as np
# import math
import collections
import sys
input = sys.stdin.readline

H,W,N = map(int,input().split())

ab = []

eff = collections.defaultdict(int)

for i in range(N):
    temp = list(map(int,input().split()))
    ab.append(temp)
    for j in range(3):
        for k in range(3):
            if (temp[0]-j >= 1) & (temp[0]-j <= H-2):
                if (temp[1]-k >= 1) & (temp[1]-k <= W-2):
                    eff[(temp[0]-j,temp[1]-k)] += 1

count = collections.Counter(eff.values())

count0 = (H-2) * (W-2) - sum(count.values())

print(count0)
for i in range(1,10):
    if i in count:
        print(count[i])
    else:
        print(0)
