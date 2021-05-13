#!/usr/bin/env python3
(n, m), *a = [[*map(int, i.split())] for i in open(0)]
like = [0] * m
for i in a:
    for j in i[1:]:
        like[j - 1] += 1
print(sum(i == n for i in like))
