x = int(input())

y = x // 11
z = x % 11

ans = 0
ans += y * 2
if z > 6:
  ans += 2
elif z > 0:
  ans += 1
  
print(ans)