N = int(input())
A = [0]
A += list(map(int, input().split()))
A += [0]
cost = [abs(A[i] - A[i+1]) for i in range(N+1)]
sumcost = sum(cost)
for i in range(1, N+1):
    print(sumcost - (cost[i-1] + cost[i]) + abs(A[i+1] - A[i-1]))
