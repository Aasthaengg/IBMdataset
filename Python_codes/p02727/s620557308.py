from heapq import heapify, heappop, heappush

x, y, a, b, c = map(int, input().split())

p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))
r = [-x for x in r]

p.sort()
q.sort()
r.sort()

p = p[-x:]
q = q[-y:]

heapify(p)
heapify(q)
heapify(r)

is_p = True
is_q = True

while is_p and is_q and r:
    pp = heappop(p)
    qq = heappop(q)
    rr = heappop(r)

    if pp <= qq:
        heappush(q, qq)
        if pp < -rr:
            heappush(p, -rr)
        else:
            is_p = False
            heappush(p, pp)
            heappush(r, rr)
    else:
        heappush(p, pp)
        if qq < -rr:
            heappush(q, -rr)
        else:
            is_q = False
            heappush(q, qq)
            heappush(r, rr)

print(sum(p) + sum(q))