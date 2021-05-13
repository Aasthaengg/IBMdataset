X = int(input())
ans = 1
i = 2
while i * i <= X:
  a = i
  while a * i <= X:
    a *= i
  ans = max(ans, a)
  i += 1
print(ans)