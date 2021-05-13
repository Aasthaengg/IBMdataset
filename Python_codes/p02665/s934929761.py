
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from itertools import combinations
from itertools import permutations
import bisect,math,heapq
alphabet = "abcdefghijklmnopqrstuvwxyz"
n = int(input())
a= list(map(int , input().split()))
s = sum(a)
f = 1
if n == 0:
  if a[0] != 1:
    print(-1)
    exit()
  else:
    print(1)
    exit()
elif a[0]!=0:
  print(-1)
  exit()
ans = 1
node = 1
for i in range(1,n+1):
  node=min(2*node, s)
  ans+=node
  node-=a[i]
  s-=a[i]
  if node < 0:
    print(-1)	
    exit()
if f: print(ans)


