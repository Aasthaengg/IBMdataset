from itertools import product
N=int(input())

F=[]
P=[]

for n in range(N):
    F.append(list(map(int,input().split())))
    
for n in range(N):
    P.append(list(map(int,input().split())))

ans=-10**10
for p in product(range(2),repeat=10):
    if len(set(p))==1 and p[0]==0:
        continue
    p_ = 0
    for idx,f in enumerate(F):
        c=0
        for i in range(10):
            c += f[i]*p[i]
        p_ += P[idx][c]
        
    if ans < p_:
        ans=p_
        
print(ans)
