#!/usr/bin/env python

nm = []
ml = []
nl = []

n, m, l = input().split()
n = int(n)
m = int(m)
l = int(l)

for i in range(n):
    r = input()
    rSplit = r.split()
    for j in range(m):
        rSplit[j] = int(rSplit[j])
    nm.append(rSplit)

for i in range(m):
    r = input()
    rSplit = r.split()
    for j in range(l):
        rSplit[j] = int(rSplit[j])
    ml.append(rSplit)

for i in range(n):
    nlrow = []
    for k in range(l):
        value = 0
        for j in range(m):
            value += nm[i][j]*ml[j][k]
        nlrow.append(value)
    nl.append(nlrow)

for i in range(n):
    for j in range(l):
        nl[i][j] = str(nl[i][j])

for x in nl:
    print(" ".join(x))