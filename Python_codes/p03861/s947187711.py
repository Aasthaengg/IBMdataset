import sys
from collections import Counter
from collections import deque
import math
import fractions
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

a,b,x=mp()
print(b//x-(a-1)//x)