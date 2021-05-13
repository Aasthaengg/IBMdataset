s = list(input())[:-1]
while True:
  l = len(s)
  h = int(l / 2)
  if l % 2 == 0 and s[:h] == s[h:]:
    break
  s.pop()
print(l)