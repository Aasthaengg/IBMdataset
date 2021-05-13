N, K = map(int, input().split())
P = dict()
C = dict()

for i, p in enumerate(map(int, input().split())):
    P[i+1] = p
for i, c in enumerate(map(int, input().split())):
    C[i+1] = c

ans = -float("inf")
for pos in range(1, N+1):
    i = pos
    score = 0
    for k in range(1, K+1):
        i = P[i]
        score += C[i]
        ans = max(ans, score)
        if i == pos:
            if score > 0:
                lastAns = score * ((K//k)-1)
                NumberOfCycle = (K%k) + k
                lastScore = lastAns
                j = i
                for _ in range(NumberOfCycle):
                    j = P[j]
                    lastScore += C[j]
                    lastAns = max(lastAns, lastScore)
                ans = max(ans, lastAns)
            break
print(ans)
