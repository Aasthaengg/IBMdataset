import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N = int(input())
Ps = list(mapint())

S = Ps[:]
S.sort()

cnt = 0
for p, s in zip(Ps, S):
    if not p==s:
        cnt += 1

if cnt>2:
    print('NO')
else:
    print('YES')