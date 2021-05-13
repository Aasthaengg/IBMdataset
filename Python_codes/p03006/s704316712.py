n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
ans=n
for i in range(n):
    for j in range(n):
        if i<j:
            p=l[i][0]-l[j][0]
            q=l[i][1]-l[j][1]
            kai=n
            for x in range(n):
                for y in range(n):
                    if l[x][0]-l[y][0]==p and l[x][1]-l[y][1]==q:
                        kai-=1
            ans=min(ans,kai)
print(ans)