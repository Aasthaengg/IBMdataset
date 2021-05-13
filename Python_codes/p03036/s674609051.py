r, D, x2000 = map(int, input().split())
result = []
for i in range(10):
  if i == 0:
    result.append(r*x2000-D)
    continue
  result.append(r*result[i-1]-D)
[print(i) for i in result]