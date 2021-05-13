import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = sorted(list(mapint()))
Bs = sorted(list(mapint()))
Cs = sorted(list(mapint()))

from bisect import bisect_left, bisect_right

ans = 0
for b in Bs:
    a_idx = bisect_left(As, b)
    c_idx = N-bisect_right(Cs, b)
    ans += a_idx*c_idx
print(ans)