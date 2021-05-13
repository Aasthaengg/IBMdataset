import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
As = list(mapint())
Bs = list(mapint())

if sum(As)<sum(Bs):
    print(-1)
else:
    diff = [a-b for a, b in zip(As, Bs)]
    diff.sort()
    cnt = 0
    need = 0
    for d in diff:
        if d>=0:
            break
        need += d
        cnt += 1
    for d in diff[::-1]:
        if need>=0:
            break
        need += d
        cnt += 1
    print(cnt)