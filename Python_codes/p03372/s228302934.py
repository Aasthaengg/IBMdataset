n,c=list(map(int,input().split()))
xv=[list(map(int,input().split())) for _ in range(n)]

cr=[0]*(n+1)
cl=[0]*(n+1)

for i in range(n):
    cr[i+1]=cr[i]+xv[i][1]
    cl[n-i-1]=cl[n-i]+xv[n-i-1][1]

leftmax=[0]*(n+1)

for i in range(n-1,-1,-1):
    leftmax[i]=max(leftmax[i+1],cl[i]-2*(c-xv[i][0]))

rightmax=[0]*(n+1)

for i in range(n):
    rightmax[i+1]=max(rightmax[i],cr[i+1]-2*xv[i][0])

ans=0
for i in range(n):
    ans=max(ans,cr[i+1]-xv[i][0]+leftmax[i+1])
    ans=max(ans,cl[n-i-1]-c+xv[n-i-1][0]+rightmax[n-i-1])

print(ans)