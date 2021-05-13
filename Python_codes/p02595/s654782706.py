n, d = map(int, input().split())
lst = [[int(j) for j in input().split()] for i in range(n)]
count = 0
for x in lst:
  distance = (x[0]**2 + x[1]**2)**0.5
  if distance <= d:
    count += 1
print(count)
