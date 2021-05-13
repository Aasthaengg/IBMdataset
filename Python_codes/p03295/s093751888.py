n,m=map(int,input().split())
claim=[0]*m
for i in range(m):
    claim[i]=list(map(int,input().split()))
claim=sorted(claim,key=lambda x:x[1])
right=claim[0][1]
count=1
for i in range(1,m):
    if claim[i][0]>=right:
        count+=1
        right=claim[i][1]
print(count)