k, s = map(int, input().split())

count = 0
for x in range(0, k+1, 1):
  for y in range(0, k+1, 1):
    total = x+y
    answer = s-total
    if 0 <= answer and answer <= k:
      count += 1
print(count)