# -*- coding: utf-8 -*-
n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]

if n==1:
    print(1)
    exit()

def cost(p,q):
    e = 0
    for i in range(n):
        for j in range(n):
            v = xy[i]
            u = xy[j]
            if p==u[0]-v[0] and q==u[1]-v[1]:
                e += 1
                break
    return n-e

res = 10**9
for i in range(n):
    for j in range(n):
        if i==j:
            continue
        v = xy[i]
        u = xy[j]
        res = min(res, cost(v[0]-u[0], v[1]-u[1]))

print(res)