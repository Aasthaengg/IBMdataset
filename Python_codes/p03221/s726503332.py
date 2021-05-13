# ABC113 D 

N,M=map(int,input().split())

P=[[] for _ in [0]*(N+1)]

for i in range(M):
    p,y=map(int,input().split())
    P[p].append((y,i))
    
from bisect import bisect_left as bl

res=[]
for p in range(N+1):
    Y=P[p][:]
    if not Y:
        continue
    
    sortY=sorted(list(set(Y)))
        
    zatY=[]
    for t_y in Y:
        zatY.append(bl(sortY,t_y))
    
    for index in zatY:
        y,i=sortY[index]
        num=10**12+p*10**6+index+1
        res.append((str(num)[1:],i))

res=[y for y,i in sorted(res,key=lambda x:x[1])]
print(*res,sep='\n')