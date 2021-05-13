n = int(input())
l = list(map(int,input().split()))
cost = [float('inf')]*(n+1)
cost[0]= 0
cost[1]=abs(l[0]-l[1])
for i in range(n):
  if i==1:
  	cost[i]=abs(l[i-1]-l[i])
  if i>1:
  	cost[i]=min(cost[i],cost[i-2]+abs(l[i]-l[i-2]),cost[i-1]+abs(l[i]-l[i-1]))
print(cost[n-1])
