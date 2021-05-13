n = int(input())
result = 0
for x in range(100):
  if (1 << x) <= n and n <= (1 << (x+1)):
    result = 1 << x

print(result)