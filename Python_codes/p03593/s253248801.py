import sys
h,w=map(int,input().split())
a=[list(input()) for i in range(h)]
l=[chr(i) for i in range(97, 97+26)]
ctl=[0]*26
for i in range(h):
  for j in range(w):
    ctl[l.index(a[i][j])]+=1

if h%2==0 and w%2==0:
  ct1=0;ct2=0;ct4=h*w
elif h%2==1 and w%2==1:
  ct1=1;ct2=h+w-2;ct4=h*w-ct1-ct2
elif h%2==0 and w%2==1:
  ct1=0;ct2=h;ct4=h*w-ct2
else:
  ct1=0;ct2=w;ct4=h*w-ct2
ct2=ct2//2;ct4=ct4//4

for i in range(26):
  while ctl[i]>=4 and ct4!=0:
    ctl[i]-=4
    ct4-=1
  if ct4==0:
    break
if ct4!=0:
  print('No')
  sys.exit()

for i in range(26):
  while ctl[i]>=2 and ct2!=0:
    ctl[i]-=2
    ct2-=1
  if ct2==0:
    break
if ct2!=0:
  print('No')
  sys.exit()

for i in range(26):
  while ctl[i]>=1 and ct1!=0:
    ctl[i]-=1
    ct1-=1
  if ct1==0:
    break
if ct1!=0:
  print('No')
  sys.exit()

print('Yes')