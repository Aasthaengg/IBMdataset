import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, A, B = mapint()
Hs = [int(input()) for _ in range(N)]
l, r = 0, 10**9+1
while r-l>1:
    half = (l+r)//2
    cum = 0
    for i in range(N):
        h = Hs[i]
        if h<=half*B:
            continue
        cum += -(-(h-half*B)//(A-B))
    if cum>half:
        l = half
    else:
        r = half

print(r)