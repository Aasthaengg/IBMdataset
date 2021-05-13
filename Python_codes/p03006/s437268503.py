n=int(input())
l=[list(map(int,input().split())) for i in range(n)]
a=[]
for i in range(n):
    for j in range(n):
        if i!=j:
            a.append([l[i][0]-l[j][0],l[i][1]-l[j][1]])
#print(a)
m=len(a)
ans=0
for k in range(m):
    c=0
    p=a[k][0]
    q=a[k][1]
    for i in range(n):
        for j in range(n):
            if i!=j and [l[i][0]-l[j][0],l[i][1]-l[j][1]]==[p,q]:
                c+=1
    ans=max(ans,c)
if n==1:
    print(1)
else:
    print(n-ans)

