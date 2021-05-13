import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M, C = mapint()
Bs = list(mapint())
ans = 0
for _ in range(N):
    p = [a*b for a, b in zip(mapint(), Bs)]
    if sum(p)+C>0:
        ans += 1
print(ans)