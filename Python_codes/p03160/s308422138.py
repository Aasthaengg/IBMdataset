N = int(input())

h = list(map(int,input().split()))
cost = [float("inf")]*N
cost[0] = 0
for i in range(N-1):
    a = abs(h[i+1]-h[i])
    if (cost[i]+a) < cost[i+1]:
        cost[i+1] = cost[i]+a
    if N - 2 > i :
        b = abs(h[i+2]-h[i])
        if (cost[i]+b) < cost[i+2]:
            cost[i+2] = (cost[i]+b)
print(cost[N-1])