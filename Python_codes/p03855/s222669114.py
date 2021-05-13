import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,k,l = list(map(int, input().split()))
from collections import defaultdict
ns0 = defaultdict(list)
ns1 = defaultdict(list)
for i in range(k):
    p,q = map(int, input().split())
    p-=1;q-=1
    ns0[p].append(q)
    ns0[q].append(p)
for i in range(l):
    p,q = map(int, input().split())
    p-=1;q-=1
    ns1[p].append(q)
    ns1[q].append(p)
def sub(ns):
    seen = [None]*n
    num = 1
    for i in range(n):
        if seen[i] is not None:
            continue
        q = [i]
        seen[i] = num
        while q:
            u = q.pop()
            for v in ns[u]:
                if seen[v] is not None:
                    continue
                seen[v] = num
                q.append(v)
        num += 1
    return seen

s1 = sub(ns0)
s2 = sub(ns1)

import gc
del ns0, ns1
gc.collect()

d1 = [None]*(max(s1)+1)
d2 = [None]*(max(s2)+1)
def update(d,ind,i):
    if d[ind] is None:
        d[ind] = set([i])
    else:
        d[ind].add(i)
for i in range(n):
    update(d1,s1[i],i)
    update(d2,s2[i],i)
#     d1[s1[i]].add(i)
#     d2[s2[i]].add(i)
d = {}
ans = [None]*n
for i in range(n):
    u,v = s1.pop(), s2.pop()
    if (u,v) not in d:
        d[u,v] = len(d1[u] & d2[v])
    ans[-(i+1)] = d[u,v]
write(" ".join(map(str, ans)))