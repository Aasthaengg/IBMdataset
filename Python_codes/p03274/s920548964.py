import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

N, K = mapint()
Xs = list(mapint())

pos = []
neg = []

for x in Xs:
    if x>=0:
        pos.append(x)
    else:
        neg.append(-x)

neg = neg[::-1]

ans = 10**18
if len(pos)>=K:
    ans = min(ans, pos[K-1])
if len(neg)>=K:
    ans = min(ans, neg[K-1])
lenp = len(pos)
lenn = len(neg)
if lenn>0:
    for i in range(min(lenp, K)):
        if K-(i+1)<=lenn:
            ans = min(ans, pos[i]*2+neg[K-i-2])
if lenp>0:
    for i in range(min(lenn, K)):
        if K-(i+1)<=lenp:
            ans = min(ans, neg[i]*2+pos[K-i-2])
print(ans)