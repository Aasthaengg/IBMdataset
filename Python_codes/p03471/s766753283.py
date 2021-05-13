N, Y = map(int, input().split())

result = []
for a in range(N+1):
  for b in range(N+1):
    c = max(N - a - b, 0)
    total = a * 10000 + b * 5000 + c * 1000
    if (total == Y) and (a + b + c == N):
      result.append([a, b, c])

if len(result) == 0:
  print("-1 -1 -1")
else:
  print(" ".join(map(str, result[0])))