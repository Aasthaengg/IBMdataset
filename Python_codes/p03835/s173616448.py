K, S = map(int, input().split())
result = 0
for x in range(min(K, S)+1):
  for y in range(min(S-x, K)+1):
    result += (0<=S-x-y<=K)
print(result)