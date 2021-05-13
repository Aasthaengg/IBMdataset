a, b, c, d = map(int, input().split())

area_1 = a*b
area_2 = c*d

if area_1 <= area_2:
  ans = area_2
else:
  ans = area_1

print(ans)