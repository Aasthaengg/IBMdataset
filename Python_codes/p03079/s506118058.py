import sys,heapq
from collections import deque,defaultdict
printn = lambda x: sys.stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG = True # and False
def ddprint(x):
  if DBG:
    print(x)

a,b,c = inm()
print('Yes' if a==b and b==c  else 'No')
