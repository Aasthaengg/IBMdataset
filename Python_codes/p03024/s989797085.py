#temprate
from sys import setrecursionlimit
setrecursionlimit(10**6)
from collections import Counter
def inputlist(): return [int(i) for i in input().split()]
#temprate

S = list(input())
c = Counter(S)
if 0<=c['x']<=7:
    print("YES")
else:
    print("NO")