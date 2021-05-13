import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,q = map(int,input().split())
d = [{} for _ in range(n)]
for i in range(m):
    l,r = map(int,input().split())
    l -= 1
    r -= 1
    if r not in d[l].keys():
        d[l][r] = 0
    d[l][r] += 1
for i in range(n-1)[::-1]:
    for k,v in d[i+1].items():
        if k not in d[i]:d[i][k] = 0
        d[i][k] += v
ans = [0]*q
for i in range(q):
    P,Q = map(int,input().split())
    P -= 1
    Q -= 1
    for k,v in d[P].items():
        if k <= Q:
            ans[i] += v
print('\n'.join(str(i) for i in ans))
