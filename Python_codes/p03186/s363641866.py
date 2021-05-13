a, b, c = map(int, input().split())

result = 0
available_pair = min(b,c)
result += (2 * available_pair)
b -= available_pair
c -= available_pair

if c > 0:
  result += min(c, a)
  c -= min(c, a)
  if c > 0:
    result += 1
else:
  result += b
print(result)