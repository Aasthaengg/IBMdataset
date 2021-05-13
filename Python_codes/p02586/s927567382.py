import sys
input = sys.stdin.readline

R,C,K=map(int,input().split())
J=[tuple(map(int,input().split())) for i in range(K)]

#DP0=[[0]*(C+2) for i in range(R+2)]
DP1=[[0]*(C+2) for i in range(R+2)]
DP2=[[0]*(C+2) for i in range(R+2)]
DP3=[[0]*(C+2) for i in range(R+2)]

MAP=[[0]*C for i in range(R)]

for x,y,v in J:
    MAP[x-1][y-1]=v

for i in range(R):
    for j in range(C):
        DP1[i][j]=max(DP1[i][j-1],DP1[i-1][j]+MAP[i][j],DP2[i-1][j]+MAP[i][j],DP3[i-1][j]+MAP[i][j])
        DP2[i][j]=max(DP2[i][j-1],DP1[i][j-1]+MAP[i][j])
        DP3[i][j]=max(DP3[i][j-1],DP2[i][j-1]+MAP[i][j])

ANS=0
for i in range(R):
    for j in range(C):
        ANS=max(ANS,DP1[i][j],DP2[i][j],DP3[i][j])
print(ANS)

