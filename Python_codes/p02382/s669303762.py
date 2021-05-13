from __future__ import division


def dist(vx, vy, p, n):
    if p == float("inf"):
        d = max([abs(vx[i] - vy[i]) for i in range(n)])
        return d
    d = 0
    for i in range(n):
        d += abs(vx[i]-vy[i]) ** p
    d = d ** (1/p)
    return d


n = int(raw_input())
vx = map(int, raw_input().split())
vy = map(int, raw_input().split())

print "{:.6f}".format(dist(vx, vy, 1, n))
print "{:.6f}".format(dist(vx, vy, 2, n))
print "{:.6f}".format(dist(vx, vy, 3, n))
print "{:.6f}".format(dist(vx, vy, float("inf"), n))