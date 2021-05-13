(n,q),*abpx = [list(map(int, s.split())) for s in open(0)]
ab,px = abpx[:n-1],abpx[n-1:]

from collections import defaultdict, deque
add = defaultdict(int)

for p,x in px:
    add[p] += x

links = defaultdict(set)

for a,b in ab:
    links[a].add(b)
    links[b].add(a)

passed = set()

dq = deque()
dq.append((0,1))

ans = {}

while dq:
    to_add, cur = dq.popleft()
    tmp = to_add + add[cur]
    ans[cur] = tmp
    for nx in links[cur]:
        links[nx].remove(cur)
        dq.append((tmp, nx))

print(*(ans[i] for i in range(1,n+1)))