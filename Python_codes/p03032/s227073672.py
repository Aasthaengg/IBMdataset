import sys,queue,math,copy,itertools,bisect,collections
INF = 10**9
LI = lambda : [int(x) for x in sys.stdin.readline().split()]
_LI = lambda : [int(x)-1 for x in sys.stdin.readline().split()]
NI = lambda : int(sys.stdin.readline())
N,K = LI()
dq = LI()

ans = -INF
for r in range(N+1):
    if K < N - r: continue

    ret = 0
    for i in range(N-r+1):
        q = dq[:i] + dq[i+r:]
        ret = sum(q)
        q.sort()
        for j in range(K - (N-r)):
            if j >= len(q)-1 : break
            if q[j] < 0:
                ret -= q[j]
            else:
                break
        ans = max(ans,ret)
print(ans)
