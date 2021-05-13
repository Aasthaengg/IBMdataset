distances = list(map(int, input().split()))
distances.sort()
ans = 0
for i in range(2):
  ans += distances[i]
print(ans)