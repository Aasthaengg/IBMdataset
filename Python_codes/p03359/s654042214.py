a, b = map(int, input().split())
ans = 0

for i in range(1, a+1):
  day = b if i == a else 31
  for j in range(1, day+1):
    if i == j:
      ans += 1

print(ans)