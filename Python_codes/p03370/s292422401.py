N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]
result = len(m)
X -= sum(m)
while X >= min(m):
  result += 1
  X -= min(m)
print(result)