import numpy as np
H,W,K=map(int, input().split())
now=0
S=[]
for i in range(H):
    s=list(input())
    S.append(s)
ans=[[0]*W for _ in range(H)]
ans=np.array(ans)

for i in range(H):
    noberry=(not "#" in S[i])
    if not noberry:
        now+=1
    berrys=0
    for j in range(W):
        if noberry and i==H-1:
            ans[i,j]=ans[i-1,j]
            continue
        if noberry and i>=1 and (ans[i-1,:]).sum()!=0:
            ans[i,j]=ans[i-1,j]
            continue
    
        if not noberry:
            
            if S[i][j]==".":
                ans[i,j]=now
            else:
                berrys+=1
                if berrys>=2:
                    now+=1
                    ans[i,j]=now
            ans[:i+1,j][ans[:i+1,j]==0]=now
for a in ans:
    print(*a)
