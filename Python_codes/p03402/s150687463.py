A,B = map(int,input().split())
grid = 100
tizu = []
for i in range(grid):
  tori = ["."] * 100
  tizu.append(tori)
a = 0
b = 0
if A == 1:
  tizu[1][0] = "#"
while A > 1:
  tizu[0+b][1+a] = "#"
  tizu[1+b][0+a] = "#"
  tizu[1+b][1+a] = "#"
  a += 2
  A -= 1
  if a >= 98:
    b += 2
    a = 0
a = 0
b = 0
while B > 1:
  tizu[99-b][0+a] = "#"
  a += 2
  B -= 1
  if a >= 98:
    b += 2
    a = 0
print(grid,grid)
for i in range(grid):
  print(''.join(tizu[i]))