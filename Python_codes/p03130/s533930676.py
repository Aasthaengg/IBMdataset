# coding: utf-8
L=[0 for i in range(4)]

for i in range(3):
    a,b=map(int,input().split())
    L[a-1]+=1
    L[b-1]+=1

cnt1=0
cnt2=0

for i in range(4):
    if L[i]==1:
        cnt1+=1
    elif L[i]==2:
        cnt2+=1

if cnt1==cnt2==2:
    print("YES")
else:
    print("NO")