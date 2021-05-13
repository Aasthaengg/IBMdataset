h,w,a,b=map(int,input().split())
ans=[['0']*w for _ in range(h)]
if a==0:
  for i in range(b):
    for j in range(w):
      ans[i][j]='1'
elif b==0:
  for i in range(h):
    for j in range(a):
      ans[i][j]='1'
else:
  for i in range(b):
    for j in range(a):
      ans[i][j]='1'
  for i in range(b,h):
    for j in range(a,w):
      ans[i][j]='1'
for i in range(h):
  print(''.join(ans[i]))