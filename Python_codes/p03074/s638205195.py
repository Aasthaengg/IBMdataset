from itertools import *

N,K=map(int,input().split())
S=input()

C=[]
now=1
cnt=0
for i in range(N):
  if S[i]==str(now):
    cnt+=1
  else:
    C.append(cnt)
    now=1-now
    cnt=1
C.append(cnt)
if len(C)%2==0:
  C.append(0)

S=[0]+list(accumulate(C))

m=len(C)
ans=0
for i in range(0,m,2):
  left=i
  right=min(i+2*K+1,m)
  ans=max(ans,S[right]-S[left])

print(ans)
