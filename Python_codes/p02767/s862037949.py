n = int(input())
x = list(map(int,input().split()))

m = min(x)
M = max(x)
ans = 10**9
for i in range(m,M+1):
  cost = 0
  for j in range(n):
    cost += (x[j]-i)**2
    
  ans = min(ans,cost)
print(ans)