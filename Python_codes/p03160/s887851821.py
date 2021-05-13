n = int(input())
arr = list(map(int, input().split()))

cost = [0]*n

cost[0] = 0
cost[1] = abs(arr[1]-arr[0])
for i in range(2, n):
  cost[i] = min(cost[i-1] + abs(arr[i] - arr[i-1]), cost[i-2] + abs(arr[i] - arr[i-2]))
  
print(cost[-1])