n,a,b = map(int,input().split())
x = list(map(int,input().split()))
cost = [0]*n
cost[1] = min((x[1]-x[0])*a,b)
for i in range(2,n):
    cost[i] = min(cost[i-1]+(x[i]-x[i-1])*a,cost[i-1]+b)
print(cost[n-1])