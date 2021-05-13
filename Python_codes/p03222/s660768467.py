H,W,K=map(int,input().split())

dpW=[[1,0]for i in range(9)]
for i in range(1,9):
    dpW[i][0]=dpW[i-1][0]+dpW[i-1][1]
    dpW[i][1]=dpW[i-1][0]
#print(dpW)

dpH=[[0 for i in range(W+2)]for j in range(H+1)]
dpH[0][1]=1

for i in range(1,H+1):
    for j in range(1,W+1):
        
        dpH[i][j]+=dpH[i-1][j]*dpW[W-j][0]*dpW[j-1][0]
        if W-j-1>=0:
            dpH[i][j]+=dpH[i-1][j+1]*dpW[W-j-1][0]*dpW[j-1][0]
        if j-2>=0:
            dpH[i][j]+=dpH[i-1][j-1]*dpW[W-j][0]*dpW[j-2][0]
        dpH[i][j]%=(10**9+7)
print(dpH[H][K])