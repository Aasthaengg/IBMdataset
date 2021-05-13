N, M = map(int, input().split())
L = []
R = []
for _ in range(M):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)
max_L = max(L)
min_R = min(R)
ans = min_R - max_L + 1
if ans > 0:
    print(ans)
else:
    print(0)
