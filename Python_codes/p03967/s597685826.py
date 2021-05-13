s = input()
g = 0
p = 0
for i in range(len(s)):
  if s[i] == 'g':
    g += 1
  else:
    p += 1
print(g - (g + p - 1) // 2 - 1)
