n = int(input())
arr = list(map(int, input().split()))
  
cost = [0]*n
cost[0] = 0
for i in range(1, n):
  if i > 1:
    cost[i] = min(abs(arr[i]-arr[i-2])+cost[i-2], abs(arr[i]-arr[i-1])+cost[i-1])
  elif i == 1:
    cost[i] = abs(arr[i]-arr[i-1])

print(cost[-1])