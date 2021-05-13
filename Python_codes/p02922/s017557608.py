a, b = map(int, input().split())
s = 1
i = 0
while s < b:
  s = s + a - 1
  i += 1
print(i)