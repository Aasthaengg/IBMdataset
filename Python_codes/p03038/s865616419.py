import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
As = list(mapint())
As.sort()

BC = [list(mapint()) for _ in range(M)]
BC.sort(key=lambda x: x[1])

cum = 0
for b, c in BC[::-1]:
    if c<As[0]:
        break
    As.extend([c]*b)
    cum += b
    if cum>=N:
        break

As.sort(reverse=True)
print(sum(As[:N]))