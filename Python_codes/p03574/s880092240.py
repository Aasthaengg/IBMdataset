H, W = map(int, input().split())
zlst = [0] * (W + 2)
b1 = []
b1.append(zlst)
for h in range(H):
  lst1 = [0]
  str1 = input()
  for s in str1:
    if s == '.':
      lst1.append(0)
    else:
      lst1.append(1)
  lst1.append(0)
  b1.append(lst1)
b1.append(zlst)

#nboard = [[] for i in range(H)]
for i in range(H):
  nstr = ''
  for j in range(W):
    if b1[i + 1][j + 1] == 1:
      nstr = nstr + '#'
    else:
      nstr = nstr + str(
        b1[i][j] + b1[i][j+1] + b1[i][j+2] + b1[i+1][j] + 
        b1[i+1][j+2] + b1[i+2][j] + b1[i+2][j+1] + b1[i+2][j+2])
  print(nstr)

