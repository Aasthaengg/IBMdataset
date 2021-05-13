k, s = map(int, input().split())

result = 0
for x in range(k+1):
  for y in range(min(s-x+1, k+1)):
    if (s-x-y) <= k:
      result += 1

print(result)