import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
S = list(input())
from itertools import accumulate

Es = [0]*(N+1)
Ws = [0]*(N+1)
for i, s in enumerate(S, 1):
    if s=='E':
        Es[i] = 1
    else:
        Ws[i] = 1
Es = list(accumulate(Es))
Ws = list(accumulate(Ws))

ans = 10**18
for i in range(1, N+1):
    w = Ws[i-1]
    e = (Es[-1]-Es[i])
    ans = min(ans, w+e)
print(ans)