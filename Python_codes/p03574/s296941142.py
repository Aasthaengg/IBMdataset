from itertools import product
H,W=list(map(int, input().split()))
M=[list(input()) for _ in range(H)]
S=set(product([-1,0,1],repeat=2))-{(0,0)}

for i in range(H):
  for j in range(W):
    if M[i][j]=='#':
      continue
    c=0
    for k in S:
      h=i+k[0]
      w=j+k[1]
      if 0<=h<H and 0<=w<W:
        if M[h][w]=='#':
          c+=1
    M[i][j]=str(c)
for i in range(H):
  print(''.join(M[i]))