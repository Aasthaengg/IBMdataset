x = int(input())

if x <= 3:
  print(x)
  exit()

ans = 0
for i in range(2, int(x**0.5)+1):
  s = i
  t = 1
  while s < x:
    t += 1
    s = i**t
    if ans < s and s <= x: ans = s
print(ans)