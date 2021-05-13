# coding: utf-8
# Your code here!
import sys
from collections import Counter
import numpy as np
n=int(input())
S=[]
for i in range(n):
    S.append(input())
s=Counter(S)
keys, values = zip(*s.most_common())

values=np.array(values)
index=np.where(values==np.max(values))
answer=[]
for i in index[0]:
    answer.append(keys[i])
answer.sort()
for i in answer:
    print(i)