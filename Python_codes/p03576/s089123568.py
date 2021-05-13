import heapq

n, k = map(int,input().split())
X = [list(map(int,input().split())) for i in range(n)]

Y = [[j for j in i] for i in X]
Z = [[j for j in i] for i in X]

X.sort()
Y.sort(key=lambda x:x[1])

ans = float("inf")
for i in range(n):
    x0 = X[i][0]
    for j in range(n):
        y0 = Y[j][1]
        Q = []
        x1_ind = 0
        for p in range(n):
            if len(Q) == k:
                break
            else:
                if X[p][0] >= x0 and X[p][1] >= y0:
                    heapq.heappush(Q, [-X[p][1], X[p][0], X[p][1]])
                    x1_ind = p
        if len(Q) == k:
            x1 = X[x1_ind][0]
            pop = heapq.heappop(Q)
            y1 = -pop[0]
            heapq.heappush(Q, pop)
            ans = min(ans, (x1-x0) * (y1-y0))
            st = x1_ind
            for p in range(st+1, n):
                if X[p][0] >= x0 and X[p][1] >= y0:
                    heapq.heappush(Q, [-X[p][1], X[p][0], X[p][1]])
                    x1 = X[p][0]
                    heapq.heappop(Q)
                    pop = heapq.heappop(Q)
                    y1 = -pop[0]
                    heapq.heappush(Q, pop)
                    ans = min(ans, (x1-x0) * (y1-y0))
print(ans)