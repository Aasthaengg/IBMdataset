import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())
Bs = list(mapint())

rest = 0
ans = 0
for i in range(N):
    a = As[i]
    b = Bs[i]
    if a>=rest:
        a -= rest
        ans += rest
    else:
        ans += a
        a = 0
    if b>=a:
        rest = b-a
        ans += a
    else:
        rest = 0
        ans += b

ans += min(rest, As[-1])

print(ans)