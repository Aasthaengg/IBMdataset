n, *a = map(int, open(0).read().split())
a = [0] + a + [0]
cost = [abs(a[i]-a[i+1]) for i in range(n+1)]
sum_cost = sum(cost)
next_cost = [abs(a[i]-a[i+2]) for i in range(n)]
for i in range(n):
    print(sum_cost-cost[i]-cost[i+1]+next_cost[i])