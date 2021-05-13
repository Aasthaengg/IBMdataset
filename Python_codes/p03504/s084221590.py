import sys
input = sys.stdin.readline
N,C=map(int,input().split())
lena=10**5+1
a=[[0]*lena for _ in range(C+1)]
for i in range(N):
    s,t,c=map(int,input().split())
    a[c][s]+=1
    a[c][t]+=-1
#print(a)
for i in range(C+1):
    for j in range(1,lena):
        a[i][j]+=a[i][j-1]
#print(a)
for i in range(C+1):
    for j in range(1,lena):
        if a[i][j]==1:
            a[i][j-1]=1
#print(a)

for i in range(lena):
    for j in range(1,C+1):
        a[j][i]+=a[j-1][i]

ans=0
#print(a)
for i in range(lena):
    ans=max(ans,a[C][i])
print(ans)
