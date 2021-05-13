n=int(input())
arr=list(map(int, input().split()))
cost=[0 for _ in range(n+1)]
cost[2]=abs(arr[1]-arr[0])
for stone in range(3, n+1):
    cost[stone]=min(cost[stone-1]+abs(arr[stone-1]-arr[stone-2]), cost[stone-2]+abs(arr[stone-1]-arr[stone-3]))
print(cost[n])