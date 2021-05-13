from collections import defaultdict
dct=defaultdict(int)
dct2=defaultdict(int)

h,w=map(int,input().split())
for i in range(h):
  s=input()
  for j in range(w):
    dct[s[j]]+=1


for k,v in dct.items():
  dct2[4]+=v//4
  dct2[2]+=v//2-2*(v//4)
  dct2[1]+=v%2


f=0

if h%2==0 and w%2==0:
  if dct2[1]==dct2[2]==0:
    f=1
elif h%2==1 and w%2==1:
  if dct2[1]==1 and dct2[4]>=((h-1)*(w-1))//4:
    f=1
elif h%2==1:
  if dct2[1]==0 and dct2[4]>=((h-1)*(w))//4:
    f=1
else:
  if dct2[1]==0 and dct2[4]>=((w-1)*(h))//4:
    f=1

if f==1:print("Yes")
else:print("No")