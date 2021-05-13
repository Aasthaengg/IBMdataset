N, K = map(int, input().split())

P = list(map(int, input().split()))
C = list(map(int, input().split()))

for i in range(len(P)):
    P[i] -= 1

ans = float("-inf")
for i in range(N):
    cycle = []
    pos = i
    total = 0
    while True:
        pos = P[pos]
        cycle.append(C[pos])
        total += C[pos]
        if pos == i: break

    l = len(cycle)
    t = 0
    for j in range(l):
        t += cycle[j]
        if j + 1 > K: break
        now = t

        if total > 0:
            cnt = (K-j-1) // l
            now += total * cnt
        ans = max(ans, now)
print(ans)             