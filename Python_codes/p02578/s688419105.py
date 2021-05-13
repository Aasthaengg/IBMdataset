n = int(input())
height = list(map(int,input().split()))

standard = height[0]
ans = 0
for i in range(n):
  if height[i] > standard:
    standard = height[i]
  elif height[i] < standard:
    ans += standard - height[i]

print(ans)