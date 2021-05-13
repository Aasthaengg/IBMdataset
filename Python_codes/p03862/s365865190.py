import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, x = mapint()
As = list(mapint())

last = As[0]
ans = 0
for i in range(1, N):
    a = As[i]
    if last+a>x:
        diff = (last+a)-x
        ans += diff
        last = max(0, a-diff)
    else:
        last = a
print(ans)