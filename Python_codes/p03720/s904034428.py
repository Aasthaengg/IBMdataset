n,m=map(int,input().split())
l=[0]*n
for i in range(m):
    p,q=map(int,input().split())
    l[p-1]+=1
    l[q-1]+=1
print(*l,sep='\n')