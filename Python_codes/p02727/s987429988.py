x, y, a, b, c = map(int, input().split())
p = sorted(map(int, input().split()))
q = sorted(map(int, input().split()))
r = sorted(map(int, input().split()), reverse=True)
pi = len(p) - x
qi = len(q) - y
ri = 0
for _ in range(len(r)):
    if r[ri] <= min(p[min(pi, len(p)-1)], q[min(qi, len(q)-1)]):
        break
    else:
        if pi >= len(p) and qi >= len(q):
            break
        else:
            if pi < len(p) and qi < len(q):
                if p[pi] < q[qi]:
                    p[pi] = r[ri]
                    pi += 1
                else:
                    q[qi] = r[ri]
                    qi += 1
            elif pi < len(p) and qi >= len(q):
                p[pi] = r[ri]
                pi += 1
            else:
                q[qi] = r[ri]
                qi += 1
            ri += 1
print(sum(p[-x:]) + sum(q[-y:]))