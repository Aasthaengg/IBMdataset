import sys
m,k=map(int,input().split())
if 2**m<=k:
  print(-1)
  sys.exit()
if m==1 and k==1:
  print(-1)
  sys.exit()
if m==1 and k==0:
  print('0 0 1 1')
  sys.exit()
if m==0:
  print('0 0')
  sys.exit()

l=[]
for i in range(2**m):
  if i!=k:
    l.append(str(i))
print(' '.join(l+[str(k)]+list(reversed(l))+[str(k)]))