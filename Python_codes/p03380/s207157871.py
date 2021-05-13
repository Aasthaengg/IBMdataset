import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())
As.sort()
M = As.pop()

diff = 10**18
for a in As:
    if abs(M/2-a)<diff:
        diff = abs(M/2-a)
        ans = a

print(M, ans)