from collections import Counter

n, k, l = map(int, input().split())
ps = [tuple(map(int, input().split())) for _ in range(k)]
rs = [tuple(map(int, input().split())) for _ in range(l)]

def root(n, u):
    if u[n] == n:
        return n
    u[n] = root(u[n], u)
    return u[n]

union1 = {x:x for x in range(1, n+1)}
for p, q in ps:
    union1[root(p, union1)] = root(q, union1)

union2 = {x:x for x in range(1, n+1)}
for r, s in rs:
    union2[root(r, union2)] = root(s, union2)

gs = {x:(root(x, union1), root(x, union2)) for x in range(1, n+1)}
c = Counter(gs.values())
print(' '.join(str(c[gs[x]]) for x in range(1, n+1)))
