import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, M = mapint()
As = list(mapint())

cnt = 0
ALL = sum(As)
for a in As:
    if 4*M*a>=ALL:
        cnt += 1

if cnt>=M:
    print('Yes')
else:
    print('No')