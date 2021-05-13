import sys
readline = sys.stdin.readline
sys.setrecursionlimit(10**8)
mod = 10**9+7
#mod = 998244353
INF = 10**18
eps = 10**-7

N,M = map(int,readline().split())

PY = [list(map(int,readline().split())) + [i] for i in range(M)]

PY.sort(key=lambda x: (x[0],x[1]))

ans = [None]*M
nowp = 1
cnt = 1
for i in range(M):
    if PY[i][0] != nowp:
        cnt = 1
        nowp = PY[i][0]
    ans[PY[i][2]] = [nowp,cnt]
    cnt += 1

for i in range(M):
    print(str(ans[i][0]).zfill(6) + str(ans[i][1]).zfill(6))
