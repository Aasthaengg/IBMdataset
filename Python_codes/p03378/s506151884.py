n,m,x = map(int,input().split())
a = list(map(int,input().split()))
cost = 0
for i in range (m):
  if a[i] < x:
    cost += 1
print(min(cost,m-cost))