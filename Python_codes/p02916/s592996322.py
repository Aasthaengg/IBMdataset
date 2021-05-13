n = int(input())
dishes = list(map(int, input().split()))
points = list(map(int, input().split()))
bonuses = list(map(int, input().split()))

score = 0
prev = 0
for i in dishes:
  score += points[i-1]
  if prev > 0:
    if i == prev + 1: score += bonuses[i-2]
  prev = i

print(score)
