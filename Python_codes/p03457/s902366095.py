#!/usr/bin/env python3
#
# Author: Tetsuya Ishikawa <tiskw111@gmail.com>
# Date  : June 30, 2020
##################################################### SOURCE START #####################################################

def manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])

N = int(input().strip())
ts = [None for _ in range(N+1)]
ps = [None for _ in range(N+1)]

ts[0] = 0
ps[0] = (0, 0)

for n in range(1, N+1):
    t, p, q = tuple(map(int, input().strip().split()))
    ts[n] = t
    ps[n] = (p, q)

for n in range(N):
    dt = ts[n+1] - ts[n]
    dist = manhattan(ps[n+1], ps[n])
    if (dist > dt) or (dt % 2) != (dist % 2):
        print("No")
        exit()

print("Yes")

##################################################### SOURCE FINISH ####################################################
# vim: expandtab tabstop=4 shiftwidth=4 fdm=marker
