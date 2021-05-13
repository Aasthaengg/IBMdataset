import sys
import copy
import math
import itertools
S = input()
tmp=753
for i in range(len(S)):
    if abs(int(S[i:i+3])-753)<tmp:
        tmp=abs(int(S[i:i+3])-753)
print(tmp)
