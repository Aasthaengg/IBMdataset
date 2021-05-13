#coding: utf-8
from collections import defaultdict
import sys

N, M = (int(x) for x in input().split())
freq = defaultdict(int)

for i in range(M):
    a, b = (int(x) for x in input().split())
    freq[a] += 1
    freq[b] += 1

for k in freq:
    if freq[k] % 2 == 1:
        print ("NO")
        sys.exit(0)

print ("YES")
