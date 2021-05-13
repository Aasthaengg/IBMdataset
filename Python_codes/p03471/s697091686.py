n, y = map(int, input().split())
ans = ''
for i in range(n + 1):
  for j in range(n + 1 - i):
    k = n - i  - j
    if 10000 * i + 5000 * j + 1000 * k == y:
      ans = f'{i} {j} {k}'
      break
  if ans:
    break
print(ans if ans else '-1 -1 -1')