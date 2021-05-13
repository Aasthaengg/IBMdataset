import sys
import itertools
# import numpy as np
import time
import math
 
sys.setrecursionlimit(10 ** 7)
 
from collections import defaultdict
 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

# map(int, input().split())
# list(map(int, input().split()))

N = int(input())
S = input()
N = len(S)

ans = 0
for i in range(N):
    if S[i:i+3] == "ABC":
        ans += 1
print(ans)