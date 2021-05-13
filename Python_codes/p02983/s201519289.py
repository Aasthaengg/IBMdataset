l,r = map(int, input().split())

if r-l >= 2019:
  print(0)
  exit()

ans = float('inf')
for i in range(l, r):
  for j in range(i+1, r+1):
  	t = i*j%2019
  	ans = min(ans,t)
print(ans)