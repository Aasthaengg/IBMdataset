N, M = [int(x) for x in input().split()]
H = [int(x) for x in input().split()]
AB = [[int(x) for x in input().split()] for _ in range(M)]

tenbo = [[] for j in range(N + 1)]

for a, b in AB:
    tenbo[a].append(b)
    tenbo[b].append(a)

ans = 0
for i in range(1, N + 1):
    x = H[i - 1]
    f = True
    for t in tenbo[i]:
        if x > H[t - 1]:
            continue
        else:
            f = False
            break
    if f:
        ans += 1

print(ans)

