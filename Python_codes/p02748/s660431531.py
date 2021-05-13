A,B,M=map(int,input().split())
at=list(map(int,input().split()))
bt=list(map(int,input().split()))
xyc=[list(map(int,input().split())) for i in range(M)]

minc=min(at)+min(bt)

for i in range(M):
    minc=min(minc,at[xyc[i][0]-1]+bt[xyc[i][1]-1]-xyc[i][2])
    
print(minc)