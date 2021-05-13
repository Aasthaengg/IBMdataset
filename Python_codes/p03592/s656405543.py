n,m,k=map(int,input().split())
flg=0
for i in range(n):
  tmp=k-m*i
  if n==i*2 or tmp<0:
    pass
  elif tmp%(n-i*2)==0 and 0<=tmp//(n-i*2)<=m:
    flg=1
if flg==1:
  print('Yes')
else:
  print('No')