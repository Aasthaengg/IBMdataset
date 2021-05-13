import itertools
import sys
import numpy as np
import collections

S=input()
wc=0
cnt=0
for i , s in enumerate(S):
    if s=='W':
        if i!=wc:
            cnt += i-wc
        wc += 1
    else:
        continue
print(cnt)
