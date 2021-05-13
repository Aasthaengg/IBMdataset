INF = 10**20
N = int(input())
height = list(map(int, input().split()))
cost = [INF]*N
cost[0] = 0
cost[1] = min(cost[1], cost[0]+abs(height[1]-height[0]))
for i in range(2, N):
  cost[i] = min(cost[i], cost[i-1]+abs(height[i]-height[i-1]), cost[i-2]+abs(height[i]-height[i-2]))
print(cost[N-1])