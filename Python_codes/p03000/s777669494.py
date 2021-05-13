import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, X = mapint()
Ls = list(mapint())

now = 0
cnt = 0
for l in Ls:
    if now>X:
        break
    now += l
    cnt += 1
else:
    if now<=X:
        cnt += 1
print(cnt)