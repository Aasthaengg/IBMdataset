#!/usr/bin/env python3
from math import ceil
S = input()
w = int(input())
print(''.join(S[i * w] for i in range(ceil(len(S) / w))))
