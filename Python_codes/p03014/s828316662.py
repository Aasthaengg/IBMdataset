h,w=map(int,input().split())
s=[input()+'#' for i in range(h)]
s.append('#'*(w+1))
h1=[[0]*(w+1) for i in range(h+1)]
w1=[[0]*(w+1) for i in range(h+1)]
for j in range(h):
  r=0
  for i in range(w+1):
    if s[j][i]=='#':
      for k in range(i-r,i+1):
        h1[j][k]=r
      r=0
      h1[j][i]=0
    else:
      r+=1
for j in range(w):
  r=0
  for i in range(h+1):
    if s[i][j]=='#':
      for k in range(i-r,i+1):
        w1[k][j]=r
      r=0
      w1[i][j]=0
    else:
      r+=1
ans=0
for i in range(h):
  for j in range(w):
    ans=max(ans,h1[i][j]+w1[i][j]-1)
print(ans)