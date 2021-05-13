R,G,B,N = map(int,input().split())

ans = 0
balls = N
for r in range(0,(balls//R)+1):
  balls_r = balls - R*r
  for g in range(0,(balls_r//G)+1):
    balls_g = balls_r - G*g
    if (balls_g >= 0) and (balls_g % B == 0):
      ans += 1

print(ans)