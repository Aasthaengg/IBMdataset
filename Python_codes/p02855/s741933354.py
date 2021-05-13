H, W, K = map(int, input().split())
S = [input() for x in range(H)]
output = [[0 for a in range(W)] for b in range(H)]

count = 0

for i in range(H):
  for j in range(W):
    s = S[i][j]
    if s == '#':
      count += 1
      output[i][j] = count
      left = '.'
      right = '.'
      
      sw = 0
      while left == '.':
        sw += 1
        if j - sw < 0 or S[i][j-sw] == '#':
          left = ''
        else:
          left = S[i][j-sw]
        if left == '.':
          output[i][j-sw] = count
      sw = 0
      while right == '.':
        sw += 1
        if j + sw > W-1 or S[i][j+sw] == '#':
          right = ''
        else:
          right = S[i][j+sw]
        if right == '.':
          output[i][j+sw] = count

last = 0
for i in range(H):
  if 0 in output[i]:
      output[i] = output[last]
  else:
    last = i


for i in range(H):
  revi = H-i-1
  if 0 in output[revi]:
      output[revi] = output[last]
  else:
    last = revi

for i in range(H):
  print(' '.join(map(str, output[i])))