N,M=map(int,input().split())
p=[0]+list(map(int,input().split()))

P=[i for i in range(N+1)]
S=[1 for i in range(N+1)]

def find(a):
    if a==P[a]:
        return a
    else:
        return find(P[a])
        
def union(b,c):
    B=find(b)
    C=find(c)
    if S[B]<S[C]:
        P[B]=P[C]
        S[C]+=S[B]
    else:
        P[C]=P[B]
        S[B]+=S[C]
        
for i in range(M):
    x,y=map(int,input().split())
    union(x,y)
#print(P)
D={}

for i in range(1,N+1):
    D[p[i]]=i
    
#print(D2)
ans=0
for i in range(1,N+1):
    if find(i)==find(D[i]):
        ans+=1
print(ans)