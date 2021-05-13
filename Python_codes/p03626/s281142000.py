n = int(input())
s1 = list(input())
s2 = list(input())
code = []

i = 0
while i < len(s1):
  if s1[i] == s2[i]:
    code.append('S')
    i += 1
  else:
    code.append('D')
    i += 2

mod = 1000000007
if code[0] == 'S':
  ptn = 3
else:
  ptn = 6
for i in range(1, len(code)):
  x, y = code[i-1], code[i]

  if x == 'S' and y == 'S':
    ptn = (ptn * 2) % mod
  elif x == 'S' and y == 'D':
    ptn = (ptn * 2) % mod
  elif x == 'D' and y == 'D':
    ptn = (ptn * 3) % mod
  elif x == 'D' and y == 'S':    
    ptn = ptn
print(ptn)
