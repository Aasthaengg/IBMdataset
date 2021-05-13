x, y = map(int, input().split())
a = x
i = 1
while (a <= y):
  a *= 2
  if a > y:
    break
  i += 1
print(i)