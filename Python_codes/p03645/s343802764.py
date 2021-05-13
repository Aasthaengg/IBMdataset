n,m=map(int,input().split())
a=[0]*(n+1)
b=[0]*(n+1)
flg=0
for i in range(m):
  p,q=map(int,input().split())
  if (p==1 and q==n) or (p==n and q==1):
    flg=1
  elif p==1:
    a[q]=1
  elif q==1:
    a[p]=1
  elif p==n:
    b[q]=1
  elif q==n:
    b[p]=1
for i in range(1,n+1):
  if a[i]==1 and b[i]==1:
    flg=1
if flg==1:
  print('POSSIBLE')
else:
  print('IMPOSSIBLE')