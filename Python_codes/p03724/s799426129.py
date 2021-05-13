N,M=map(int,input().split())
G=[]
x=dict()
for i in range(M):
    a,b=map(int,input().split())
    if a in x:
        x[a]+=1
    else:
        x[a]=1
    if b in x:
        x[b]+=1
    else:
        x[b]=1

flag=True
for idx in x:
    if x[idx]%2==0:
        pass
    else:
        flag=False

if flag:
    print("YES")
else:
    print("NO")