M, D = map(int, input().split())
ans = 0
for i in range(1, M+1):
  for j in range(10, D+1):
    d1 = j%10
    d10 = j//10
    if d1 >= 2 and d10 >= 2:
      if i == d1 * d10:
        ans += 1
print(ans)