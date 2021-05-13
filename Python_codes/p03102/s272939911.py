a,b,c=map(int,input().split())
d=list(map(int,input().split()))
e=[]
for i in range(a):
    e.append(list(map(int,input().split())))
ans=0
for i in range(a):
    result=0
    for j in range(b):
        result+=d[j]*e[i][j]
    result+=c
    if result>0:
        ans+=1
print(ans)




