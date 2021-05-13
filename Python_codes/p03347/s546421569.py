import sys
import os,io
input=io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
n=int(input())
a=[]
s=int(input())
if s!=0:
  print(-1)
  sys.exit()
a.append(s)
ans=0
prev=0
for i in range(n-1):
  x=int(input())
  if x-prev>1:
    print(-1)
    sys.exit()
  if x-prev==1:
    ans+=1
  else:
    ans+=x
  prev=x
print(ans)