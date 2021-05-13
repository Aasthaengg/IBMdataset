N = int(input())
cost = []
for i in range(N):
    cost.append(int(input()))
cost.sort(reverse=True)
sum_cost = cost[0]//2 + sum(cost[1:])
print(sum_cost)