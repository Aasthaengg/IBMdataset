import sys

icase=0
if icase==0:
    n=int(input())
    a=[[0]*n for i in range(n)]
    for i in range(n):
        a[i]=list(map(int,input().split()))
elif icase==1:
    n=3
    a=[[0, 1, 3], [1, 0, 2], [3, 2, 0]]
#    a=[[0, 1, 3], [1, 0, 1], [3, 1, 0]]

dp=[[0]*n for i in range(n)]
for i in range(n):
    dp[i]=a[i].copy()
    
c=[[0]*n for i in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if dp[i][j]>dp[i][k]+dp[k][j]:
                dp[i][j]=dp[i][k]+dp[k][j]
            if dp[i][j]==dp[i][k]+dp[k][j] and i!=k and j!=k:
                c[i][j]=1                
                

icnt=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if a[i][j]!=dp[i][j]:
            print(-1)
            sys.exit()
        elif c[i][j]==0:
            icnt+=dp[i][j]
print(icnt)