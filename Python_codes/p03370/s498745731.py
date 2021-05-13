# -*- coding: utf-8 -*-
N, X = list(map(int, input().split()))
m = []
for i in range(N):
    m.append(int(input()))
    
ans = len(m)

X -= sum(m)
ans += X//min(m)
print(ans)