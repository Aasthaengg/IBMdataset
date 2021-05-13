N, M = map(int, input().split())
l, r = 1, N
for i in range(M):
    L, R = map(int, input().split())
    l, r = max(l, L), min(r, R)
if r - l >= 0:
    print(min(r - l + 1, N))
else:
    print(0)