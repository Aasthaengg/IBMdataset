
#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np

def int_mtx(N):
    x = []
    for _ in range(N):
        x.append(list(map(int,input().split())))
    return np.array(x)

N = int(input())

a = int_mtx(N)
visit = [0]*(N+1)
now = 1
visit[now] = 1

ans = 0

for i in range(0,N):
    ans += 1
    now = a[now-1][0]
    if now == 2:
        print(ans)
        exit()
    if visit[now] == 1:
        print(-1)
        exit()
    visit[now] = 1





