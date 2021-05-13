import numpy as np

N = int(input())
H = list(map(int, input().split()))

max_ = 0
for h in H:
    max_ = max(max_,h)
    if h <= max_-2:
        print('No')
        exit()
else:
    print('Yes')
