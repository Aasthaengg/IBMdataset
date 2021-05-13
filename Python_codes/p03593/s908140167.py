H,W=map(int,input().split())
Cr = []
for _ in range(H):
  Cr += list(input())
  
from collections import Counter
Cr=Counter(Cr)

cntod=0
cnt4=0

for cr in Cr.most_common():
  c=cr[1]
  if c%2==1:
    cntod+=1
    cnt4+=(c-1)//4
  else:
    cnt4+=c//4
ret = 'No'
if H%2==0 and W%2==0:
  if cntod==0 and cnt4==(H*W)//4:
    ret = 'Yes'
if H%2==0 and W%2==1:
  if cntod==0 and cnt4>=(H*(W-1))//4:
    ret = 'Yes'
if H%2==1 and W%2==0:
  if cntod==0 and cnt4>=((H-1)*W)//4:
    ret = 'Yes'
if H%2==1 and W%2==1:
  if cntod==1 and cnt4>=((H-1)*(W-1))//4:
    ret = 'Yes'
print(ret)