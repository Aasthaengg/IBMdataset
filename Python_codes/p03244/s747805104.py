n=int(input())
v=list(map(int,input().split()))
from collections import Counter
v_odd=Counter([v[i] for i in range(n) if i%2==0])
v_eve=Counter([v[i] for i in range(n) if i%2==1])
v_eve[-1]=0
v_odd[-1]=0

eve=[[k,v] for k,v in v_eve.items()]
odd=[[k,v] for k,v in v_odd.items()]
eve.sort(key=lambda x:x[1])
odd.sort(key=lambda x:x[1])

if eve[-1][0]!=odd[-1][0]:
  print(n-eve[-1][1]-odd[-1][1])
else:
  ans0=n-eve[-2][1]-odd[-1][1]
  ans1=n-eve[-1][1]-odd[-2][1]
  print(min(ans0,ans1))