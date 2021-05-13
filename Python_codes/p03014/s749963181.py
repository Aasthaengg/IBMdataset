h,w=map(int,input().split())
s=[input() for _ in range(h)]
hdp=[[0]*w for _ in range(h)] # hdp[i][j]:i,jマスに明かりを置いた時のてらせる縦マス数
wdp=[[0]*w for _ in range(h)] # wdp[i][j]:i,jマスに明かりを置いた時のてらせる横マス数
for i in range(h):
  for j in range(w):
    if s[i][j]=='#':
      continue
    if j>0 and wdp[i][j-1]>0:
      wdp[i][j]=wdp[i][j-1]
    else:
      for k in range(j,w):
        if s[i][k]=='#':
          break
        wdp[i][j]+=1
    if i>0 and hdp[i-1][j]>0:
      hdp[i][j]=hdp[i-1][j]
    else:
      for k in range(i,h):
        if s[k][j]=='#':
          break
        hdp[i][j]+=1
ans=0
for i in range(h):
  for j in range(w):
    ans=max(ans,hdp[i][j]+wdp[i][j]-1)
print(ans)
