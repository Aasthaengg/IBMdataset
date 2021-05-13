n=int(input())
h=list(map(int,input().split()))
cost=[0,abs(h[1]-h[0])]
for i in range(2,n):
  cost.append(min(cost[i-2]+abs(h[i]-h[i-2]),cost[i-1]+abs(h[i]-h[i-1])))
print(cost[n-1])
