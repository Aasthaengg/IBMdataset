import numpy as np

H,W=map(int,input().split())

s=np.zeros((H+2,W+2),dtype=int)

for i in range(H):
    s0=input()
    for j in range(W):
        if s0[j]==".":
            num=0
        elif s0[j]=="#":
            num=1
        
        s[i+1][j+1]=num
        

ans_s=s[1:H+1,1:W+1]

ans=0
for k in range(1,H+1):
    for l in range(1,W+1):
        if s[k][l]==1:
            if s[k-1][l]==0 and s[k+1][l]==0 and s[k][l-1]==0 and s[k][l+1]==0:
                ans=1
                break

if ans==1:
    print("No")
else:
    print("Yes")