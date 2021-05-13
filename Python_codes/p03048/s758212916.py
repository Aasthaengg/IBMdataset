r,g,b,n = map(int,input().split())
ans = 0
for i in range(3001):
  for j in range(3001):
    buy = i*r + j*g
    if n - buy < 0:
      break
    elif (n - buy)%b == 0:
      ans += 1
print(ans)
