N = int(input())
C=list(input())
W=(C.count('W'))
R=N-W
WW=0
RR=0
X=[0]*(N-1)
if W>0 and R>0:
  for i in range(N-1):
    if C[i]=='W':
      WW+=1
    RR=(N-i-1)-(W-WW)
    X[i]=max(WW,RR)
print(min(X))