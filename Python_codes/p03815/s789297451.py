x = int(input())

ans = 2 * (x // 11)

if x % 11 == 0:
  pass
elif x % 11 < 7:
  ans += 1
else:
  ans += 2
print(ans)