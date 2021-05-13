m, n, x = map(int,input().split())
al = list(map(int,input().split()))


cost = 0
for i in range(x,m+1):
  if i in al:
    cost += 1

cost2 = 0
for i in range(x,0,-1):
  if i in al:
    cost2 += 1
    
print(min(cost, cost2))
