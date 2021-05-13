N, M, C = map(int, input().split(' '))

B = list(map(int, input().split(' ')))

result = 0

for i in range(1, N+1):
  values = list(map(int, input().split(' ')))
  count = 0
  for idx, v in enumerate(values):
    count += v * B[idx]
  count += C

  if count > 0:
    result += 1

print(result)
