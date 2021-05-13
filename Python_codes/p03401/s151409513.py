n = int(input())
a = [0]
a.extend(list(map(int,input().split())))
a.append(0)

cost = []

for i in range(n):
  cost.append(abs(a[i+1]-a[i]))
cost.append(abs(a[-2]))

s_cost = sum(cost)
for i in range(n):
  print(s_cost - cost[i]- cost[i+1] + abs(a[i+2]-a[i]))