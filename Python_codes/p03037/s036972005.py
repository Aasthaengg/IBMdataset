N, M = [int(a) for a in input().split()]
L = []
R = []

for _ in range(M):
    l, r = [int(a) for a in input().split()]
    L.append(l)
    R.append(r)

mingate = max(L)
maxgate = min(R)
ans = max(maxgate - mingate + 1, 0)
print(ans)