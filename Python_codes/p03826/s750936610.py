a, b, c, d = map(int, input().split())

s_1 = a * b
s_2 = c * d

if s_1 == s_2:
  print(s_2)
else:
  print(max(s_1, s_2))