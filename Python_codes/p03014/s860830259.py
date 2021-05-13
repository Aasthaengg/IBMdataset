h,w=map(int,input().split())
s=[input() for _ in range(h)]
a=[[0]*w for _ in range(h)]
for i in range(h):
  cnt=0
  for j in range(w):
    if s[i][j]=='.':cnt+=1
    else:
      for k in range(cnt):
        a[i][j-k-1]=cnt
      cnt=0
  for k in range(cnt):
    a[i][j-k]=cnt
for i in range(w):
  cnt=0
  for j in range(h):
    if s[j][i]=='.':cnt+=1
    else:
      for k in range(cnt):
        a[j-k-1][i]+=cnt
      cnt=0
  for k in range(cnt):
    a[j-k][i]+=cnt
ans=0
for i in range(h):
  for j in range(w):
    ans=max(ans,a[i][j])
print(ans-1)