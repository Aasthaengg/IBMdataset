import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,copy,functools
import time,random

sys.setrecursionlimit(10**7)
inf = 10**20
eps = 1.0 / 10**10
mod = 10**9+7
mod2 = 998244353
dd = [(-1,0),(0,1),(1,0),(0,-1)]
ddn = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(): return [list(map(int, l.split())) for l in sys.stdin.readlines()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()
def pf(s): return print(s, flush=True)
def pe(s): return print(str(s), file=sys.stderr)
def JA(a, sep): return sep.join(map(str, a))
def JAA(a, s, t): return s.join(t.join(map(str, b)) for b in a)


def main():
    start = time.time()
    n,m,p = LI()
    abc = [LI() for _ in range(m)]
    er = collections.defaultdict(set)
    err = collections.defaultdict(set)
    for a,b,c in abc:
        er[b].add(a)
        err[a].add(b)

    v = set([n])
    q = [n]
    qi = 0
    while len(q) > qi:
        t = q[qi]
        qi += 1
        for b in er[t]:
            if b not in v:
                v.add(b)
                q.append(b)

    u = set([1])
    q = [1]
    qi = 0
    while len(q) > qi:
        t = q[qi]
        qi += 1
        for b in err[t]:
            if b not in u:
                u.add(b)
                q.append(b)

    v &= u

    e = collections.defaultdict(list)
    for a,b,c in abc:
        if a not in v or b not in v:
            continue
        e[a].append((b,c-p))

    en = len(e)
    km = sum(map(lambda x: x[2], abc))
    def search(s):
        d = collections.defaultdict(lambda: -inf)
        vc = collections.defaultdict(int)
        q = []
        d[s] = 0
        heapq.heappush(q, (0, s))
        ttt = 0
        while len(q):
            ttt += 1
            if ttt % 1024 == 0:
                if time.time() - start > 1.5:
                    return
            mk, u = heapq.heappop(q)
            k = -mk
            if d[u] > k:
                continue
            if k > km or vc[u] > en:
                return
            vc[u] += 1

            for uv, ud in e[u]:
                vd = k + ud
                if d[uv] < vd:
                    d[uv] = vd
                    heapq.heappush(q, (-vd, uv))

        return d

    d = search(1)
    if d is None:
        return -1
    return max(0, d[n])

print(main())



