R,G,B,N = map(int,input().split())

ans = 0
for r in range(3010):
  red = r * R
  if N < red:
    break
  
  for g in range(3010):
    green = g * G
    blue = N - red - green
    if blue < 0:
      break
    if blue % B == 0:
      ans += 1
      
print(ans)
