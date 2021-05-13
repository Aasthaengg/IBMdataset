n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
d_a={}
d_b={}
flg=0
for i in range(n):
  d_a[a[i]]=d_a.get(a[i],0)+1
for i in range(m):
  d_b[b[i]]=d_b.get(b[i],0)+1
for i in b:
  c=d_a.get(i,0)
  if c < d_b[i]:
    flg=1
if flg == 1:
  print('NO')
else:
  print('YES')