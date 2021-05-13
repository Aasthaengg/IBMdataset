import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

s=input()
for i in range(len(s)):
    if i%2==0 and s[i]=="L":
        print("No")
        exit()
    if i%2==1 and s[i]=="R":
        print("No")
        exit()
print("Yes")
