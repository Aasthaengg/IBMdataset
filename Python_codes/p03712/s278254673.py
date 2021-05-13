h, w = map(int, input().split())
a = []
a.append('#'*(w+2))
for i in range(1, h+1):
  a.append('#'+ input() + '#')
a.append('#'*(w+2))
for i in range(h+2):
  print(a[i])