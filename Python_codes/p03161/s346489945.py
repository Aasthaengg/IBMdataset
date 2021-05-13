(N,K) = map(int,input().split())
h = list(map(int,input().split()))
n = 2
cost = [0]*N
cost[1] = abs(h[1]-h[0])
for n in range(2,N):
    costmin = 10**10
    for i in range(max(0,n-K),n):
        costmin = min(costmin,cost[i]+abs(h[n]-h[i]))
    cost[n] = costmin
    
print(cost[N-1])