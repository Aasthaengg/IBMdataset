n = int(input())
ans = n
L = [list(map(int, input().split())) for _ in range(n)]
pq = []
for i in range(n):
    for j in range(i+1, n):
        pq.append([L[j][0] - L[i][0], L[j][1] - L[i][1]])
for p, q in pq:
    cost = n
    for x, y in L:
        if [x-p, y-q] in L:
            cost -=1
    ans = min(ans, cost)
print(ans)
