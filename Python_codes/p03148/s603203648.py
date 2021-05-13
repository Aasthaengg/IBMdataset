from heapq import heappop, heappush
from collections import defaultdict

N, K = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

# Step 1: Choose greedy
X.sort(key=lambda x: -x[1])
pq = []
chosen = defaultdict(int)
cnt = 0
score = 0
for t, d in X[:K]:
    heappush(pq, (d, t))
    cnt += 1 if chosen[t] == 0 else 0
    chosen[t] += 1
    score += d
ans = score + cnt ** 2

# Step 2: Replace chosen items
idx = K
while pq:
    # Step 2.1
    d_p, t_p = heappop(pq)
    if chosen[t_p] <= 1:
        continue
    chosen[t_p] -= 1
    score -= d_p

    # Step 2.2
    while idx < N and chosen[X[idx][0]] != 0:
        idx += 1

    if idx == N:
        break
        
    cnt += 1
    chosen[X[idx][0]] += 1
    score += X[idx][1]
    ans = max(ans, score + cnt ** 2)
    
print(ans)

