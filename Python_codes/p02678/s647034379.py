import sys, math

input = sys.stdin.readline

N, M = map(int, input().split())
path = [set() for _ in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    path[a-1].add(b-1)
    path[b-1].add(a-1)

cost = [[math.inf, -1]]*N
cost[0] = [0, 0]
pre = [0]

for d in range(N):
    next = []
    for i in pre:
        for j in path[i]:
            if cost[j][0] != math.inf:
                continue
            cost[j] = [d, i]
            next.append(j)
    pre = next
    if len(next)==0:
        break

if max(cost)[0] == math.inf:
    print('No')
    sys.exit()

print('Yes')
for d, pre_idx in cost[1:]:
    print(pre_idx+1)
