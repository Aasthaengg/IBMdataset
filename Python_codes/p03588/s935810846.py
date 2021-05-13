# coding: utf-8

N = int(input())
L = []
p1 = 0
p2 = float('inf')
r1 = float('inf')
r2 = 0
for i in range(N):
    a, b = map(int,input().split())
    L.append([a, b])
    r1 = min(a, r1)
    p1 = max(b, p1)
    r2 = max(a, r2)
    p2 = min(b, p2)

ans = r2
for i in range(N):
    if L[i][0] == r2:
        ans += L[i][1]
print(ans)