import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())
As.sort()
from itertools import accumulate
cumAs = list(accumulate([0]+As))

ans = 0
cum = 0
for i in range(N-1):
    a = As[i]
    cum += a
    if cum*2<As[i+1]:
        ans = 0
    else:
        ans += 1

print(ans+1)