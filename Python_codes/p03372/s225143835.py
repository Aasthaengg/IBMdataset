import sys
input=sys.stdin.readline
import copy
N,C=map(int,input().split())
L=[]
for i in range(N):
    x,v=map(int,input().split())
    L.append([x,v])

LR=copy.deepcopy(L)
L=[[0,0]]+L
#print(L)
LR=LR[::-1]

for i in range(N):
    LR[i][0]=C-LR[i][0]
LR=[[0,0]]+LR
#print(LR)
Lr=[0]
S=0
for i in range(1,N+1):
    S+=L[i][1]
    Lr.append(S-L[i][0])
#print(Lr)
LC=[0]

for i in range(1,N+1):
    LC.append(max(LC[-1],Lr[i]))
#print(LC)

LRr=[0]
S=0
for i in range(1,N+1):
    S+=LR[i][1]
    LRr.append(S-LR[i][0])
#print(LRr)
LRC=[0]
for i in range(1,N+1):
    LRC.append(max(LRC[-1],LRr[i]))
#print(LRC)

ans=0
for i in range(N+1):
    cnt=LC[i]-L[i][0]+LRC[N-i]
    ans=max(ans,cnt)
for i in range(N+1):
    cnt=LRC[i]-LR[i][0]+LC[N-i]
    ans=max(ans,cnt)
print(ans)