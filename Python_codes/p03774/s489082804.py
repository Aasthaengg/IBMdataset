n,m=map(int,input().split())
student=[list(map(int,input().split())) for _ in range(n)]
checkpoint=[list(map(int,input().split())) for _ in range(m)]
ans=[0]*n

for i in range(n):
    distance=10**9
    index=0
    for j in range(m):
        if abs(student[i][0]-checkpoint[j][0])+abs(student[i][1]-checkpoint[j][1])<distance:
            distance=abs(student[i][0]-checkpoint[j][0])+abs(student[i][1]-checkpoint[j][1])
            index=j
    ans[i]=index+1
for i in range(n):
    print(ans[i])