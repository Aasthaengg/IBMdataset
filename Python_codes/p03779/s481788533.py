x = int(input())
ans = 0
s = 0
while s < x:
  ans += 1
  s += ans
print(ans)
