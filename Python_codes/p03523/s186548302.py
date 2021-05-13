from itertools import*
from math import*
from collections import*
from heapq import*
from bisect import bisect_left,bisect_right
from copy import deepcopy
inf = float("inf")
mod = 10**9+7
from functools import reduce
import sys
sys.setrecursionlimit(10**7)
#文字数が9文字以下のときだけ全探索
s = input()
if len(s)>9:
    print("NO")
    exit()
bool = False
for i in range(2**9):
    cur = ""
    for j in range(9):
        if (i>>j)&1:
            if (j<len(s)):
                cur +="A"+s[j]
            else:
                cur +="A"
        else:
            if j<len(s):
                cur +=s[j]
    if cur =="AKIHABARA":
        bool = True
if bool:
    print("YES")
else:
    print("NO")