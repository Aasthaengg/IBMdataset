H,W,K=map(int,input().split())
C=[input() for _ in range(H)]
ans=0
for i in range(2**H):
  for j in range(2**W):
    c=0
    for ii in range(H):
      for jj in range(W):
        if 1&(i>>ii)&(j>>jj):
          if C[ii][jj]=='#':
            c+=1
    if c==K:
      ans+=1
print(ans)