n = int(input())
ans = 0
for i in range(1,1000):
  for j in range(2, 10):
    if i**j <= n:
      ans = max(ans, i**j)
print(ans)