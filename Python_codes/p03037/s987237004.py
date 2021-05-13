N, M = map(int, input().split())
l = []
r = []
for i in range(M):
    L, R = map(int, input().split())
    l.append(L)
    r.append(R)
m = min(r) - max(l)
if m < 0:
    print(0)
else:
    print(m + 1)