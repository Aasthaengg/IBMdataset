N,M,X=map(int,input().split())
C=[]
A=[]
for _ in range(N):
    c,*a=map(int,input().split())
    C.append(c)
    A.append(a)
    
import itertools

ans=float('inf')
f=False
for i in range(1,N+1):
    for j in itertools.combinations(range(N), i):
        t=[0]*M
        c=0
        
        for k in j:
            c+=C[k]
            t=[t+a for (t,a) in zip(t,A[k])]
        #print(c,t)
        if M <= len([x for x in t if x>=X]):
            ans=min(ans,c)
            f=True
print(ans if f else -1)