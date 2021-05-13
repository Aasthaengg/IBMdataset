import sys
sys.setrecursionlimit(10**9)


def unite(par, i, j):
    j = get_par(par, j)
    par[j] = get_par(par, i)

def get_par(par, p):
    while par[p] != p:
        p = par[p]
    return par[p]

n,k,l = map(int, input().split())
pq = []
road = [i for i in range(n+1)]
rcnt = [set([i]) for i in range(n+1)]
rail = [i for i in range(n+1)]
acnt = [set([i]) for i in range(n+1)]
for i in range(k):
    p,q = map(int,input().split())
    pq.append((p,q))
    aa = get_par(road, p)
    bb = get_par(road, q)
    if aa == bb:
        continue
    # unite
    if aa < bb:
        road[bb] = aa
        rcnt[aa] |= rcnt[bb]
    else:
        road[aa] = bb
        rcnt[bb] |= rcnt[aa]

rs = []
for i in range(l):
    p,q = map(int,input().split())
    rs.append((p,q))
    aa = get_par(rail, p)
    bb = get_par(rail, q)
    if aa == bb:
        continue
    # unite
    if aa < bb:
        rail[bb] = aa
        acnt[aa] |= acnt[bb]
        # acnt[aa] += acnt[bb]
    else:
        rail[aa] = bb
        acnt[bb] |= acnt[aa]

ans = [(road[get_par(road, i)], rail[get_par(rail, i)]) for i in range(1,n+1)]
from collections import Counter
c = Counter(ans)
print(*[c[(road[get_par(road, i)], rail[get_par(rail, i)])] for i in range(1,n+1)])
# print(acnt)
# print(rcnt)
