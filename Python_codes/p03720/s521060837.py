n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
city = {}
for i in ab:
  for j in i:
    if j not in city:
      city[j] = 1
    else:
      city[j] += 1
for number in range(1, n+1):
  if number in city:
    print(city[number])
  else:
    print(0)