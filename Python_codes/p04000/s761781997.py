from collections import defaultdict
H,W,N=map(int,input().split())
d=defaultdict(int)
for n in range(N):
  y,x=map(int,input().split())
  for i in range(3):
    for j in range(3):
      if W-3>=x+i-3>=0 and H-3>=y+j-3>=0:
        d[(x+i-3,y+j-3)]+=1
ans=[0]*10
S=0
for t,t_num in d.items():
  ans[t_num]+=1
  S+=1
ans[0]=(H-2)*(W-2)-S
for i in range(10):
  print(ans[i])
