import sys
from collections import Counter
from collections import deque
import math
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

n,m=mp()
for i in range(m//n,0,-1):
    s,a=divmod(m,i)
    if a%s==0:
        print(i)
        exit()