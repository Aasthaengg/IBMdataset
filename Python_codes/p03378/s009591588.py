N, M, X = map(int, input().split())
A = list(map(int, input().split()))

cost = [0]*(N+1)

for a in A:
    cost[a-1] = 1

ans = min(sum(cost[:X]), sum(cost[X:]))

print(ans)
