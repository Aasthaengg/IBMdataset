def possible(s):
  return 8 - s.count('o') <= 15 - len(s)

s = input()
if possible(s):
  print("YES")
else:
  print("NO")