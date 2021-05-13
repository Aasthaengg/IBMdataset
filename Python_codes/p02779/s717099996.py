n = int(input())
a = sorted(list(map(int, input().split())))

b = [-1] + a

l = []
for i in range(n):
  l.append(a[i] - b[i])
  
if l.count(0) == 0:
  print('YES')
else:
  print('NO')