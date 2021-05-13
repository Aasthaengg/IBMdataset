import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, T = mapint()
Ts = list(mapint())

ans = 0
last = 0
for t in Ts:
    ans += min(t-last, T)
    last = t

print(ans+T)