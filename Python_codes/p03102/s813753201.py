n,m,c=map(int,input().split())
b=list(map(int,input().split()))
List=[]
ans=0
for i in range(n):
    code=list(map(int,input().split()))
    List.append(code)
for i in range(n):
    add=0
    for j in range(m):
        add+=List[i][j]*b[j]
    if add+c>0:
        ans+=1
print(ans)