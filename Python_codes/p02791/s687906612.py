import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Ps = list(mapint())

m = 10**18
ans = 0
for p in Ps:
    if p<=m:
        ans += 1
        m = p

print(ans)