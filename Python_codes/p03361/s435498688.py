import sys

H,W=map(int,input().split())
L=[[x for x in input()] for _ in range(H)]
ans='Yes'

for i in range(H):
  for j in range(W):
    if L[i][j]=='.':
      continue
    else:
      try:
        if L[i][j+1]=='#':
          continue
      except:
        pass
      try:
        if L[i][j-1]=='#':
          continue
      except:
        pass
      try:
        if L[i-1][j]=='#':
          continue
      except:
        pass
      try:
        if L[i+1][j]=='#':
          continue
      except:
        pass
      print('No')
      sys.exit()
      
print('Yes')