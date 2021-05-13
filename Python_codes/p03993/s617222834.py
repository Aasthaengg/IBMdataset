n=int(input())
ans=0
table=[-1]*n
for i,j in enumerate(list(map(int,input().split()))):
    if table[j-1]==-1:table[i]=j-1
    elif table[j-1]==i:ans+=1
print(ans)