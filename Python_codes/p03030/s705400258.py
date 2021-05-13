#!/usr/bin/env python3
n = int(input())
e = sorted([[str(i + 1)] + input().split() for i in range(n)],
           key=lambda x: int(x[2]),
           reverse=True)
d = dict()
for i in e:
    if i[1] not in d:
        d[i[1]] = []
    d[i[1]].append(i[0])
e = sorted(d.items(), key=lambda x: x[0])
for i in e:
    print(*i[1], sep="\n")
