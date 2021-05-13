import sys,heapq
from collections import deque,defaultdict
printn = lambda x: sys.stdout.write(x)
inn = lambda : int(input())
inl   = lambda: list(map(int, input().split()))
inm   = lambda:      map(int, input().split())
DBG =  True
def ddprint(x):
  if DBG:
    print(x)

n = inn()
od = (n%2 == 1)
print((n*n-2*n+(1 if od else 0)) // 2)
for i in range(1,n):
    for j in range(i+1,n+1):
        if i+j != (n if od else n+1):
            print("{} {}".format(i,j))
