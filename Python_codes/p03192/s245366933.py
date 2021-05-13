#template
from sys import setrecursionlimit
setrecursionlimit(10**6)
from collections import Counter
def inputlist(): return [int(j) for j in input().split()]
#template
N = list(input())
c = Counter(N)
print(c['2'])