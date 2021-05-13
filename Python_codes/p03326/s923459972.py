# -*- coding: utf-8 -*-
#D - Patisserie ABC
import sys 
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
N, M = map(int, readline().split())
data = [[] for _ in range(8)]
for _ in range(N):
    A = list(map(int,readline().split()))
    for i in range(1<<3):
        tmp = 0
        for j in range(3):
            if i>>j & 1:
                tmp+=A[j]
            else:
                tmp+=-A[j]
        data[i].append(tmp)

ans = 0
for row in data:
    row = sorted(row,reverse=True)[:M]
    total = sum(row)
    ans = max(ans,total)
print(ans)