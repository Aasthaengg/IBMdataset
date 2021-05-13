N, M, X = map(int, input().split())

C = []
A = []
for n in range(N):
    tmp = list(map(int, input().split()))
    C.append(tmp[0])
    A.append(tmp[1:])

from itertools import combinations

costs =[]
for i in range(1,N+1):
    idx = list(range(N))
    comb = list(combinations(idx,i))
    for c in comb:
        scores = [0]*M
        cost = 0
        for j in c:
            cost += C[j]
            for m in range(M):
                scores[m] += A[j][m]

            check = [int(s>=X) for s in scores]

            if sum(check)==M:
                costs.append(cost)

if len(costs)>0:
    print(min(costs))
else:
    print(-1)
