n = int(input())
ans = 0
for i in range(n + 1):
  if i * i > n:
    break
  ans = i * i
print(ans)
