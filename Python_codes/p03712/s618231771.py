h, w = map(int, input().split())
a = [list(input().split()) for _ in range(h)]
for i in a:
  i.insert(0, '#')
  i.append('#')
a.insert(0, ['#']*(w+2))
a.append(['#']*(w+2))
for i in a:
  print(''.join(i))