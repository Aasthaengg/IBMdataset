N, M = map(int, input().split())
original_data = [tuple(map(int, input().split())) for i in range(0, N)]
#print(original_data)
pattern = [
  (1, 1, 1),
  (1, -1, 1),
  (1, 1, -1),
  (-1, 1, 1),
  (-1, -1, 1),
  (-1, 1, -1),
  (1, -1, -1),
  (-1, -1, -1),
]

max_sum = 0
for p in pattern:
  res = []
  for x, y, z in original_data:
    total = x * p[0] + y * p[1] + z * p[2]
    res.append(total)
  res.sort(reverse=True)
  max_sum = max(max_sum, sum(res[:M]))
  #print(res)
print(max_sum)
