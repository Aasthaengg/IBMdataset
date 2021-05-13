n,m=map(int,input().split())
l=[]
r=[]
for i in range(m):
    tmp=list(map(int,input().split()))
    l.append(tmp[0])
    r.append(tmp[1])

print(max(min(r)-max(l)+1,0))