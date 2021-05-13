

N = int(input())
xy = [tuple(map(int, input().split())) for _ in range(N)]

pq = []
for i in range(N):
    for j in range(N):
        if i != j:
            pq.append((xy[i][0] - xy[j][0], xy[i][1] - xy[j][1]))


ans = N
for p,q in pq:
    cost = 0
    for x,y in xy:
        if  (x+p, y+q) not in xy:
            cost += 1

    ans = min(ans, cost)

print(ans)