X, Y = map(int, input().split())
ans = -1
for i in range(10**8):
  Z = X*(i+2)
  if Z%Y != 0 and Z <= 10**18:
    ans = Z
    break
  if Z > 10**18:
    break
print(ans)