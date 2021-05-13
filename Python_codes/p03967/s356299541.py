s = input()
g = 0
for c in s:
  if c == 'g':
    g += 1
p = len(s) - g
print((g - p) // 2)