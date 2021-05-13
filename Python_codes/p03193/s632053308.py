#template
from sys import setrecursionlimit
setrecursionlimit(10**6)
from collections import Counter
def inputlist(): return [int(j) for j in input().split()]
#template
N,H,W = inputlist()
count = 0
for i in range(N):
    A,B = inputlist()
    if A >= H and B >= W:
        count+=1
print(count)