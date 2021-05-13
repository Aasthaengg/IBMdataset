import sys
INF = float('inf')
a,b,c,d = map(int, sys.stdin.readline().rstrip("\n").split())
l = [a,b]
r = [c,d]
ans = -INF
for ln in l:
    for rn in r:
        ans = max(ans,ln*rn)
print(ans)