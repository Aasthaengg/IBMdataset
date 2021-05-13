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

n = inn()
s = input()
r = 0
b = 0
for c in s:
    if c == 'R':
        r += 1
    else:
        b += 1

print('Yes' if r>b else 'No')
