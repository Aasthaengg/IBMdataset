S = list(input())
ans = 0
for i in S:
  if i == '+':
    ans += 1
  elif i == '-':
    ans -= 1
print(ans)