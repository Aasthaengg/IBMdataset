
# inputを高速化する。
import sys
input = sys.stdin.readline

a,b,m = map(int, input().split())

As = list(map(int, input().split()))
Bs = list(map(int, input().split()))

ans = min(As) + min(Bs)

for i in range(m):
    x,y,c = map(int, input().split())
    total = As[x-1] + Bs[y-1] - c
    ans = min(ans , total)

print(ans)