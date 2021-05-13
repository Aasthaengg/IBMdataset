# -*- coding: utf-8 -*-
import sys
from sys import stdin

N = int(stdin.readline().rstrip())
S = stdin.readline().rstrip()
count = 0
for i in range(N - 2):
  if S[i:].startswith('ABC'):
    i += 3
    count += 1
print(count)