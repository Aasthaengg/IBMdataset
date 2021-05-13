from itertools import combinations, product
N,A,B,C=map(int, input().split())
l=[int(input()) for _ in range(N)]
ans = float("inf")
for tmp in product(range(4), repeat=N):
    cost = 0
    forA = []
    forB = []
    forC = []
    for i in range(N):
        if tmp[i] == 0:
            forA.append(l[i])
            cost += 10
        elif tmp[i] == 1:
            forB.append(l[i])
            cost += 10
        elif tmp[i] == 2:
            forC.append(l[i])
            cost += 10
    if not (forA and forB and forC):
        continue
    cost -= 30
    toA = sum(forA)
    toB = sum(forB)
    toC = sum(forC)
    cost += abs(toA - A) + abs(toB - B) + abs(toC - C)
    ans = min(ans, cost)

print(ans)