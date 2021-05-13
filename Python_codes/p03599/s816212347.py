a,b,c,d,e,f=map(int,input().split())

dp=[[False]*(f+2) for i in range(f+2)]
# dp[i][j]: iは入れた砂糖の重さ、jは水、値は濃度

dp[0][0]=True

for j in range(f+1):
    i=0
    if dp[i][j] and j<=f:
        if 0<i+j+100*a<=f:
            dp[i][j+100*a]=True
        if 0<i+j+100*b<=f:
            dp[i][j+100*b]=True

for i in range(f+1):
    for j in range(1,f+1):
        if dp[i][j] and i+j<=f:
            if 0<i+c+j<=f:
                dp[i+c][j]=True
            if 0<i+d+j<=f:
                dp[i+d][j]=True

tmpi=0
tmpj=min(a*100,b*100)
for i in range(f+1):
    for j in range(1,f+1):
        if dp[i][j] and i*100<=e*j and 0<j+i<=f and tmpi*j<i*tmpj:
            tmpi=i
            tmpj=j
        if i*100==e*j:
            break

print(tmpi+tmpj, tmpi)