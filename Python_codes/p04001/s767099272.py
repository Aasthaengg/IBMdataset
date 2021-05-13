s = input()
l = len(s)
m = [int(s[0])]
if l >= 2:
  for j in range(1,l):
    y = 0
    for k in range(1,j+1):
      y += m[k-1] + int(s[k:j+1]) *(2** (k-1))
    x = y + int(s[:j+1])
    m.append(x)
print(m[-1])

