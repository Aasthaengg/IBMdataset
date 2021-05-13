n = int(input())
s = input()
result = 0

for i in range(10):
  a = s.find(str(i))
  if a == -1:
    continue
  for i in range(10):
    b = s.find(str(i), a + 1)
    if b == -1:
      continue
    for i in range(10):
      if s.find(str(i), b + 1) != -1:
        result += 1

print(result)
