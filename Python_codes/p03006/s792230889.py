n=int(input())
L=[]
for _ in range(n):
    l=list(map(int,input().split()))
    L.append(l)
if n==1:
    print(1)
    exit()
pq=[]
ans=[]
for i in range(n-1):
    for j in range(i+1,n):
        x=L[i][0]-L[j][0]
        y=L[i][1]-L[j][1]
        if [x,y] in pq:
            ans[pq.index([x,y])] += 1
        elif [-x,-y] in pq:
            ans[pq.index([-x,-y])] += 1
        else:
            pq.append([x,y])
            ans.append(1)

print(n-max(ans))