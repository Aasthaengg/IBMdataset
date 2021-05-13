n=int(input())
a=list(map(int,input().split()))
cost=[0]*(n)
for i in range(1, n):
  if i==1:
    cost[i]=abs(a[i]-a[i-1])
  else:
    cost[i]=min(cost[i-1]+abs(a[i]-a[i-1]), cost[i-2]+abs(a[i]-a[i-2]))
print(cost[-1])