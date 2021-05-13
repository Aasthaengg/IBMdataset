H,W,A,B=map(int,input().split())

ans=[]
base="0"*A+"1"*(W-A)
nbase="1"*A+"0"*(W-A)

for i in range(B):
    ans.append(base)
for i in range(H-B):
    ans.append(nbase)

for i in range(H):
    print(ans[i])