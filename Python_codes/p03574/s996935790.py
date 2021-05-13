H,W=map(int,input().split())
S=[input() for _ in range(H)]

padded = []
for i in range(H+2):
  if i == 0 or i == H+1:
    padded.append('.'*(W+2))
  else:
    padded.append('.'+S[i-1]+'.')
    
def calc(row,col):
  out=0
  for i in range(3):
    for j in range(3):
      if padded[row-1+i][col-1+j]=='#':out+=1
  return out

ans=[[] for _ in range(H)]
for i in range(1,H+1):
  for j in range(1,W+1):
    if padded[i][j]=='#':
      ans[i-1].append('#')
      continue
    tmp = calc(i,j)
    ans[i-1].append(str(tmp))
  ans[i-1] = ''.join(ans[i-1])

for i in range(H):
  print(ans[i])