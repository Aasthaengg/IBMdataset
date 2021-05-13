n, a, b = map(int, input().split())
ans = 0
lis = []

for i in range(1, n+1):
  y = str(i)
  w = 0
  for x in range(len(y)):
    w += int(y[x])
  if a <= w <= b:
    ans += i

print(ans)
    
