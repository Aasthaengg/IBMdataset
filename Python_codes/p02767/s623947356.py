n = int(input())
points = list(map(int, input().split()))

sum = 0
for i in points:
  sum += i

mean = sum/len(points)
if mean%2 != 0:
    mean = int(round(mean,0))

ans = 0
for i in points:
  ans += (i - mean)**2

print(ans)