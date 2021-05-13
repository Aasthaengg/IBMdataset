import math

x,y = map(int,input().split())

ans = 1
a = y
for i in range(10**9) :
  if a < x or a == 1:
    break
  x_t = x
  ans_t = 1
  for j in range(10**9) :
    x_t = x_t*2
    if x_t > y :
      break
    ans_t += 1
  ans = max(ans,ans_t)
  a = math.floor(a**0.5)

print(ans)