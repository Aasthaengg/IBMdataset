X = int(input())
 
r = 0
ans = 0
while True:
  r += X
  r %= 360
  ans += 1
  if r == 0:
    break
print(ans)