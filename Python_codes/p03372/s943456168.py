import sys
def input():
    return sys.stdin.readline()[:-1]
inf=float("inf")
n,c=map(int,input().split())
xv=[list(map(int,input().split())) for i in range(n)]

ra=[0]*(n+1)
ra[1]=xv[0][1]-xv[0][0]
for i in range(1,n):
    ra[i+1]=ra[i]+xv[i][1]-(xv[i][0]-xv[i-1][0])
mra=[0]*(n+1)
mra[1]=ra[1]
for i in range(1,n):
    mra[i+1]=max(mra[i],ra[i+1])
# print(ra)
# print(mra)

lb=[0]*(n+1)
lb[1]=xv[-1][1]-(c-xv[-1][0])
for i in range(1,n):
    lb[i+1]=lb[i]+xv[-1-i][1]-(xv[-i][0]-xv[-1-i][0])
mlb=[0]*(n+1)
mlb[1]=lb[1]
for i in range(1,n):
    mlb[i+1]=max(mlb[i],lb[i+1])
# print(lb)
# print(mlb)

ans=max(0,lb[0]+mra[n])
for i in range(1,n+1):
    ans=max(ans,lb[i]+mra[n-i]-(c-xv[-i][0]))
ans=max(ans,ra[0]+mlb[n])
for i in range(1,n+1):
    ans=max(ans,ra[i]+mlb[n-i]-xv[i-1][0])
print(ans)