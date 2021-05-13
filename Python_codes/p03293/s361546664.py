# -*- coding: utf-8 -*-
from collections import deque
import sys
#input = sys.stdin.readline
def inpl(): return list(map(int, input().split()))

S = input()
T = input()

for i in range(len(S)+1):
    if S == T[i:] + T[:i]:
        print("Yes")
        break
else:
    print("No")