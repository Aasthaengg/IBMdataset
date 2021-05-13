m,k = map(int,input().split())
#m,k = 1,0
if 2**m <= k :
  print(-1)
  exit()
if (m==1 and k !=0) :
  print(-1)
  exit()
if (m==1 and k==0) :
  print('0 0 1 1')
  exit()

ret = [k]
for i in range(2**m):
  if i!=k:
    ret.append(i)
ret.append(k)
for i in reversed(range(2**m)):
  if i!=k:
    ret.append(i)
print(' '.join(map(str,ret)))