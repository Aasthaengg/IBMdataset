n = int(input())
line = list(map(int, input().split()))
min_dist = 10**9
for i in range(max(line)+1):
  sum_dist = 0
  for j in range(n):
    sum_dist += (line[j] - i)**2
  if sum_dist < min_dist:
    min_dist = sum_dist
print(min_dist)