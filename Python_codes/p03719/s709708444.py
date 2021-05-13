import sys
from collections import Counter
from collections import deque
def input(): return sys.stdin.readline().strip()
def mp(): return map(int,input().split())
def lmp(): return list(map(int,input().split()))

a,b,c=mp()
if a<=c<=b:
    print("Yes")
else:
    print("No")