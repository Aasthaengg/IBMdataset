import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = [0]+list(mapint())
As.sort()
from itertools import accumulate
cAs = list(accumulate(As))
cAs.sort(reverse=True)
As.sort(reverse=True)

ans = 1
for i in range(1, N):
    if cAs[i]*2<As[i-1]:
        break
    ans += 1

print(ans)