H, W = map(int, input().split())
dstr = '.' * (W + 2)
b1 = []
b1.append(dstr)
for h in range(H):
  str1 = '.' + input() + '.'
  b1.append(str1)
b1.append(dstr)

for i in range(1, H - 1):
  for j in range(1, W - 1):
    if b1[i][j] == '#' and b1[i-1][j] == '.' and b1[i+1][j] == '.' and b1[i][j-1] == '.' and b1[i][j+1] == '.':
      print('No')
      exit()
print('Yes')