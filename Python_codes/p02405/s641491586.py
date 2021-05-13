l = []
while True:
  h,w = map(int,input().split())
  if (h,w) == (0,0):
    break
  else:
    l.append([h,w])
for i in l:
  r1 = ''
  r2 = ''
  for j in range(i[1]//2):
    r1 += '#.'
    r2 += '.#'
  if i[1]%2 == 1:
    r1 += '#'
    r2 += '.'
  for m in range(i[0]//2):
    print(r1)
    print(r2)
  if i[0]%2 == 1:
    print(r1)
  print()