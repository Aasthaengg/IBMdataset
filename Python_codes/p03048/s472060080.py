r,b,g,m = map(int,input().split())
ans = 0
for i in range(3001):
  for j in range(3001):
    if m >= r*i+b*j and (m-r*i-b*j)%g == 0:
      ans += 1
print(ans)