X = int(input())
T = 0
ans = 0
while (1):
  T = (T+X)%360
  ans += 1
  if (T == 0):
    break
print(ans)