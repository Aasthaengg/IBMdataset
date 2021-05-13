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
xarr=sorted(xarr)
yarr=sorted(yarr)
xsums=[0]
for val in xarr:
  xsums.append(xsums[-1]+val)
ysums=[0]
for val in yarr:
  ysums.append(ysums[-1]+val)
if len(xarr)!=0:
  xmax=xarr[-1]
  xsum=xsums[-1]
else:
  xmax=0
  xsum=0
if len(yarr)!=0:
  ymax=yarr[-1]
  ysum=ysums[-1]
else:
  ymax=0
  ysum=0
x+=xsum
y+=ysum
if x%2==1 or y%2==1:
  print('No')
else:
  xdp=[0]*10000
  xdp[0]=1
  for j in range(len(xarr)):
    val=xarr[j]
    for i in range(xsums[j]+val+1,-1,-1):
      if i-val<0:
        break
      if xdp[i-val]==1:
        xdp[i]=1
  ydp=[0]*10000
  ydp[0]=1
  for j in range(len(yarr)):
    val=yarr[j]
    for i in range(ysums[j]+val+1,-1,-1):
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