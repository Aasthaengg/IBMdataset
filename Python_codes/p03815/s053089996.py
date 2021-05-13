x = int(input())
r = x // 11 * 2
if x % 11 == 0:
  pass
elif x % 11 > 6:
  r += 2
else:
  r += 1
print(r)