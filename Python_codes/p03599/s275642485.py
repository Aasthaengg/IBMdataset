#!/usr/bin/env python3
a, b, c, d, e, f = map(int, input().split())

lim = (f // c) + 1
ans_n = 0
ans_total = 0
ans_su = 0

for ac in range(31):
    for bc in range(31):

        wt = a * ac * 100 + b * bc * 100
        if wt == 0:
            break

        max_su = wt / 100 * e

        for cc in range(lim):
            for dc in range(lim):

                su = c * cc + d * dc

                if (su > max_su) or (wt + su > f):
                    break

                n = (100 * su) / (wt + su)
                if n >= ans_n:
                    ans_n = n
                    ans_total = wt+su
                    ans_su = su

print(ans_total, ans_su)
