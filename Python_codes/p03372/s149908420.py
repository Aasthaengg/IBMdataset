n,c=map(int,input().split())
l=[list(map(int,input().split())) for _ in [0]*n]
if n==1:print(max(0,l[0][1]-l[0][0]));exit()
r=[[c-x[0],x[1]] for x in l[::-1]]

L=[[0]*2 for _ in range(n)]
L[0]=[l[0][1]-l[0][0],l[0][1]-l[0][0]*2]
for i in range(n-1):
    L[i+1][0]=L[i][0]+l[i+1][1]-(l[i+1][0]-l[i][0])
    L[i+1][1]=L[i][1]+l[i+1][1]-(l[i+1][0]-l[i][0])*2
for i in range(n-1):
    L[i+1][0]=max(L[i+1][0],L[i][0])

R=[[0]*2 for _ in range(n)]
R[0]=[r[0][1]-r[0][0],r[0][1]-r[0][0]*2]
for i in range(n-1):
    R[i+1][0]=R[i][0]+r[i+1][1]-(r[i+1][0]-r[i][0])
    R[i+1][1]=R[i][1]+r[i+1][1]-(r[i+1][0]-r[i][0])*2
for i in range(n-1):
    R[i+1][0]=max(R[i+1][0],R[i][0])

max1=max(L[n-1][0],max(R[i][1]+L[n-i-2][0] for i in range(n-1)))
max2=max(R[n-1][0],max(L[i][1]+R[n-i-2][0] for i in range(n-1)))
print(max(0,max1,max2))