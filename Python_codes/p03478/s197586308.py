n, a, b = map(int, input().split())

result = 0

for x in range(1, n+1):
  if a <= sum(map(int, str(x))) <= b:
    result += x

print(result)