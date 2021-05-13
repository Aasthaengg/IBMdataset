import sys
input = sys.stdin.readline
 
t = int(input())
po = []
 
for _ in range(t):
  x,y = list(map(int,input().split()))
  po.append((x,y))
  
po.sort()
 
dp1 = [+(10**99) for _ in range(t)]
 
for i in range(t):
  x,y = po[i][0], po[i][1]
  value = x+y
  dp1[i] = min(dp1[i-1], value)
  
dp2 = [+(10**99) for _ in range(t)]
 
for i in range(t):
  x,y = po[i][0], po[i][1]
  value = x-y
  dp2[i] = min(dp2[i-1], value)
  
best = -9999999999999999999999999999
#print(dp)
 
for i in range(1,t):
  dist = po[i][0] + po[i][1] - dp1[i-1]
  best = max(best, dist)
  
  dist = po[i][0] - po[i][1] - dp2[i-1]
  best = max(best, dist)
  
print(best)