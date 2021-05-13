# ABC 103 D - Islands War
f=lambda:map(int,input().split())
N,M=f()
wars=[]
for i in range(M):
    l,r=f()
    wars.append((r,l))
wars.sort()

res=M
r,l=wars.pop(0)
for nr,nl in wars:
    if nl<r:
        res-=1
    else:
        r=nr
print(res)