x, y = map(int, input().split())

res = x
ans = 0
while res <= y:
  res = res * 2
  ans += 1
  
print(ans)