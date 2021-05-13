import sys
input = sys.stdin.readline

n,m,q= map(int, input().split())
a= [list(map(int, input().split())) for i in range(m)]
b= [list(map(int, input().split())) for i in range(q)]


# ２次元累積和
c=[[0]*(n+1) for i in range(n+1)]
for i,j in a:
    c[i][j]+=1

for i in range(1,n+1):
    for j in range(1,n+1):
        c[i][j] += c[i - 1][j]+c[i][j - 1]-c[i-1][j-1]

for i,j in b:
    ans=c[j][j]-c[i-1][j]-c[j][i-1]+c[i-1][i-1]
    print(ans)