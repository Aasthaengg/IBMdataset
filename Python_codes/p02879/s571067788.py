import sys
from collections import Counter
from collections import deque
import math
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

a,b=mp()
if a<=9 and b<=9:
    print(a*b)
else:
    print(-1)