n = int(input())
l = []
for i in range(2):
  l.append(list(map(int, input().split())))

a = []
for i in range(n):
  p = 0
  for j in range(n):   
    if i == j:
      p += l[0][j] + l[1][j]
    elif i < j:
      p += l[1][j]
    else:
      p += l[0][j]
  a.append(p)
print(max(a))