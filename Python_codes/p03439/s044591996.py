N = int(input())

print(0)
l = str(input())
if l == 'Vacant':
  exit()
print(N-1)
r = str(input())
if r == 'Vacant':
  exit()
  
left, right = 0, N-1
for i in range(20):
  n = (right+left) // 2
  print(n)
  a = str(input())
  if a == 'Vacant':
    exit()
  if (n-left) % 2 == 0:
    if l == a:
      left = n
    else:
      right = n
  else:
    if l == a:
      right = n
    else:
      left = n
      l = a
