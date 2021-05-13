n, m = map(int, input().split())
digit = ''.join(['0',str(n),'b'])
cost = [0] + [m*10**5+1] * (2**n-1)
for i in range(m):
  a, b = map(int,input().split())
  c = list(map(int, input().split()))
  cc = 0
  for j in c:
      cc += 2**(j-1)
  for j in range(2**n):
    jj = j | cc
    cost[jj] = min(cost[jj],cost[j]+a)
if cost[-1] == m*10**5+1:
  print(-1)
else:
  print(cost[-1])