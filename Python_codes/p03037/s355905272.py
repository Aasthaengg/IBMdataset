N,M=map(int,input().split())
l=[]
r=[]
for i in range(M):
    L,R=map(int,input().split())
    l.append(L)
    r.append(R)
a=max(l)
b=min(r)
x=list(range(a,b+1))
print(len(x))