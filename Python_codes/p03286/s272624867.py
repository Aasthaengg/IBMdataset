import bisect
from collections import deque

n=int(input())

ans=[0]

for i in range(2**20):
  ch=0
  for j in range(20):
    
    if (i>>j)&1:
      ch+=2**(j*2)
  ans.append(ch)
  
ans1=[]
for x in range(2**20):
  ch1=0
  for y in range(20):
    if (x>>y)&1:
      ch1+=(-2)**(y*2+1)
  ans1.append(ch1)
  

for a in ans1:
  if n-a>=0:
    d=bisect.bisect_right(ans,n-a)
    if ans[d-1]==n-a:
      ans_min=a
      ans_plus=ans[d-1]
      break
      
v=1
C=0
while v<=ans_plus:
  v*=4
  C+=2
C-=2
pl_list=[]
while C>-1:
  if ans_plus>=2**C:
    pl_list.append(1)
    ans_plus-=2**C
    C-=2
  else:
    pl_list.append(0)
    C-=2
w=-2
D=1

while ans_min<=w:
  w*=4
  D+=2
D-=2

mi_list=[]
while D>0:
  if ans_min<=(-2)**D:
    mi_list.append(1)
    ans_min-=(-2)**D
    D-=2
  else:
    mi_list.append(0)
    D-=2

ans_str=[]
P=deque(pl_list)
M=deque(mi_list)

while P or M:
  if P:
    x=P.pop()
  else:
    x=0
  if M:
    y=M.pop()
  else:
    y=0
  ans_str.append(str(x))
  ans_str.append(str(y))

ans_str_r=list(reversed(ans_str))
if len(ans_str_r)>1:
  if ans_str_r[0]=='0':
    ans_str_r.remove('0')
  
if n!=0:
  print(''.join(ans_str_r))
else:
  print(0)