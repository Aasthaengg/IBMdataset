import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())
As.sort()

from bisect import bisect_right
maxA = As[-1]
idx = bisect_right(As, maxA/2)

if abs(As[idx]-(maxA/2))>=abs(As[idx-1]-(maxA/2)):
    print(maxA, As[idx-1])
else:
    print(maxA, As[idx])