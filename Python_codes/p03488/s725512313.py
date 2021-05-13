s=input()+'T'
x,y=map(int,input().split())
if 'T' in s:
  pos=s.index('T')
  x-=pos
  s=s[pos+1:]
arr=s.split('T')
xarr=[]
yarr=[]
for i in range(len(arr)):
  l=len(arr[i])
  if l==0:
    continue
  if i%2==0:
    yarr.append(l)
  else:
    xarr.append(l)
x+=sum(xarr)
y+=sum(yarr)
if x%2==1 or y%2==1:
  print('No')
else:
  #DP for xarr,yarr
  xdp=[0]*8005
  xdp[0]=1
  for val in xarr:
    for i in range(8004,-1,-1):
      if i-val<0:
        break
      if xdp[i-val]==1:
        xdp[i]=1
  ydp=[0]*8005
  ydp[0]=1
  for val in yarr:
    for i in range(8004,-1,-1):
      if i-val<0:
        break
      if ydp[i-val]==1:
        ydp[i]=1
  if xdp[x//2]==0:
    print('No')
  else:
    if ydp[y//2]==0:
      print('No')
    else:
      print('Yes')