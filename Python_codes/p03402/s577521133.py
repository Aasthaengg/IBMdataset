a, b = map(int, input().split())

a -= 1
b -= 1
print(100, 100)
for i in range(100):
  l = []
  for j in range(100):
    c = '#' if i < 50 else '.'
    if i % 2 and j % 2:
      if i < 50 and a:
        c = '.'
        a -= 1
      if i >= 50 and b:
        c = '#'
        b -= 1
    l.append(c)
  print(''.join(l))
    
