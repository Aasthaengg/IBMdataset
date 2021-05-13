import copy
Z=[]

def dfs(A,n,m):
    global Z
    if len(A)==n:
        Z.append(copy.deepcopy(A))
        return
    
    first = A[-1] if len(A)>0 else 1
    
    for i in range(first, m+1):
        
        A.append(i)
        
        dfs(A,n,m)
        A.pop()
    

n,m,q = map(int,input().split()) 

dfs([],n,m)


A=[]
B=[]
C=[]
D=[]

for _ in range(q):
    a,b,c,d = map(int,input().split()) 
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    
ans = 0    
for z in Z:
    score=0
    for i in range(q):
        if z[B[i]-1] - z[A[i]-1] == C[i]:
            score += D[i]
            
    ans=max(ans,score)
        
    
print(ans)
