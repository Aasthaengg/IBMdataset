a, b, c = map(int, input().split())
o=0
for i in range(1, b+1):
  k = i*a
  if k%b==c:
    o+=1
if o > 0:
  print('YES')
else:
  print('NO')