import sys
input = sys.stdin.readline

x, y, a, b, c = map(int, input().split())
p = sorted(list(map(int, input().split())))
q = sorted(list(map(int, input().split())))
r = sorted(list(map(int, input().split())))

n = 0
np = 0
nq = 0
ans = 0
while n < x + y:
    cs = []
    if p and np < x:
        cs.append(p[-1])
    if q and nq < y:
        cs.append(q[-1])
    if r:
        cs.append(r[-1])
    m = max(cs)
    if r and m == r[-1]:
        ans += r.pop()
    elif p and m == p[-1]:
        ans += p.pop()
        np += 1
    else:
        ans += q.pop()
        nq += 1
    n += 1

print(ans)
